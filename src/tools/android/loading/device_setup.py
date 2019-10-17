# Copyright 2016 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

import collections
import contextlib
import logging
import os
import shutil
import subprocess
import sys
import tempfile
import time

_SRC_DIR = os.path.abspath(os.path.join(
    os.path.dirname(__file__), '..', '..', '..'))

_CATAPULT_DIR = os.path.join(_SRC_DIR, 'third_party', 'catapult')
sys.path.append(os.path.join(_CATAPULT_DIR, 'devil'))
from devil.android import device_utils
from devil.android import forwarder
from devil.android.sdk import adb_wrapper
from devil.android.sdk import intent
from devil.android.sdk import keyevent

sys.path.append(os.path.join(_SRC_DIR, 'build', 'android'))
from pylib import constants
from video_recorder import video_recorder

sys.path.append(os.path.join(_SRC_DIR, 'tools', 'perf'))
from chrome_telemetry_build import chromium_config

sys.path.append(chromium_config.GetTelemetryDir())
from telemetry.internal.image_processing import video
from telemetry.internal.util import wpr_server

sys.path.append(os.path.join(
    _CATAPULT_DIR, 'telemetry', 'third_party', 'webpagereplay'))
import adb_install_cert
import certutils

import common_util
import devtools_monitor
import emulation
import options


OPTIONS = options.OPTIONS

# The speed index's video recording's bit rate in Mb/s.
_SPEED_INDEX_VIDEO_BITRATE = 4


class DeviceSetupException(Exception):
  def __init__(self, msg):
    super(DeviceSetupException, self).__init__(msg)
    logging.error(msg)


def GetFirstDevice():
  """Returns the first connected device.

  Raises:
    DeviceSetupException if there is no such device.
  """
  devices = device_utils.DeviceUtils.HealthyDevices()
  if not devices:
    raise DeviceSetupException('No devices found')
  return devices[0]


def GetDeviceFromSerial(android_device_serial):
  """Returns the DeviceUtils instance."""
  devices = device_utils.DeviceUtils.HealthyDevices()
  for device in devices:
    if device.adb._device_serial == android_device_serial:
      return device
  raise DeviceSetupException(
      'Device {} not found'.format(android_device_serial))


def Reboot(device):
  """Reboot the device.

  Args:
    device: Device to reboot, from DeviceUtils.
  """
  # Kills the device -> host forwarder running on the device so that
  # forwarder.Forwarder have correct state tracking after having rebooted.
  forwarder.Forwarder.UnmapAllDevicePorts(device)
  # Reboot the device.
  device.Reboot()
  # Pass through the lock screen.
  time.sleep(3)
  device.SendKeyEvent(keyevent.KEYCODE_MENU)


def DeviceSubmitShellCommandQueue(device, command_queue):
  """Executes on the device a command queue.

  Args:
    device: The device to execute the shell commands to.
    command_queue: a list of commands to be executed in that order.
  """
  REMOTE_COMMAND_FILE_PATH = '/data/local/tmp/adb_command_file.sh'
  if not command_queue:
    return
  with tempfile.NamedTemporaryFile(prefix='adb_command_file_',
                                   suffix='.sh') as command_file:
    command_file.write('#!/bin/sh\n')
    command_file.write('# Shell file generated by {}\'s {}\n'.format(
        __file__, DeviceSubmitShellCommandQueue.__name__))
    command_file.write('set -e\n')
    for command in command_queue:
      command_file.write(subprocess.list2cmdline(command) + ' ;\n')
    command_file.write('exit 0;\n'.format(
        REMOTE_COMMAND_FILE_PATH))
    command_file.flush()
    device.adb.Push(command_file.name, REMOTE_COMMAND_FILE_PATH)
    device.adb.Shell('sh {p} && rm {p}'.format(p=REMOTE_COMMAND_FILE_PATH))


@contextlib.contextmanager
def ForwardPort(device, local, remote):
  """Forwards a local port to a remote one on a device in a context."""
  # If we're logging requests from a local desktop chrome instance there is no
  # device.
  if not device:
    yield
    return
  device.adb.Forward(local, remote)
  try:
    yield
  finally:
    device.adb.ForwardRemove(local)


# WPR specific attributes to set up chrome.
#
# Members:
#   chrome_args: Additional flags list that may be used for chromium to load web
#     page through the running web page replay host.
#   chrome_env_override: Dictionary of environment variables to override at
#     Chrome's launch time.
WprAttribute = collections.namedtuple('WprAttribute',
                                      ['chrome_args', 'chrome_env_override'])


@contextlib.contextmanager
def _WprHost(wpr_archive_path, record=False,
             network_condition_name=None,
             disable_script_injection=False,
             wpr_ca_cert_path=None,
             out_log_path=None):
  assert wpr_archive_path

  def PathWorkaround(path):
    # webpagereplay.ReplayServer is doing a os.path.exist(os.path.dirname(p))
    # that fails if p = 'my_file.txt' because os.path.dirname(p) = '' != '.'.
    # This workaround just sends absolute path to work around this bug.
    return os.path.abspath(path)

  wpr_server_args = ['--use_closest_match']
  if record:
    wpr_server_args.append('--record')
    if os.path.exists(wpr_archive_path):
      os.remove(wpr_archive_path)
  else:
    assert os.path.exists(wpr_archive_path)
  if network_condition_name:
    condition = emulation.NETWORK_CONDITIONS[network_condition_name]
    if record:
      logging.warning('WPR network condition is ignored when recording.')
    else:
      wpr_server_args.extend([
          '--down', emulation.BandwidthToString(condition['download']),
          '--up', emulation.BandwidthToString(condition['upload']),
          '--delay_ms', str(condition['latency']),
          '--shaping_type', 'proxy'])

  if disable_script_injection:
    # Remove default WPR injected scripts like deterministic.js which
    # overrides Math.random.
    wpr_server_args.extend(['--inject_scripts', ''])
  if wpr_ca_cert_path:
    wpr_server_args.extend(['--should_generate_certs',
        '--https_root_ca_cert_path=' + PathWorkaround(wpr_ca_cert_path)])
  if out_log_path:
    # --log_level debug to extract the served URLs requests from the log.
    wpr_server_args.extend(['--log_level', 'debug',
                            '--log_file', PathWorkaround(out_log_path)])
    # Don't append to previously existing log.
    if os.path.exists(out_log_path):
      os.remove(out_log_path)

  # Set up WPR server and device forwarder.
  server = wpr_server.ReplayServer(PathWorkaround(wpr_archive_path),
      '127.0.0.1', 0, 0, None, wpr_server_args)
  http_port, https_port = server.StartServer()[:-1]

  logging.info('WPR server listening on HTTP=%s, HTTPS=%s (options=%s)' % (
      http_port, https_port, wpr_server_args))
  try:
    yield http_port, https_port
  finally:
    server.StopServer()


def _VerifySilentWprHost(record, network_condition_name):
  assert not record, 'WPR cannot record without a specified archive.'
  assert not network_condition_name, ('WPR cannot emulate network condition' +
                                      ' without a specified archive.')


def _FormatWPRRelatedChromeArgumentFor(http_port, https_port):
  HOST_RULES='MAP * 127.0.0.1,EXCLUDE localhost'
  return [
      '--testing-fixed-http-port={}'.format(http_port),
      '--testing-fixed-https-port={}'.format(https_port),
      '--host-resolver-rules={}'.format(HOST_RULES)]


@contextlib.contextmanager
def LocalWprHost(wpr_archive_path, record=False,
                 network_condition_name=None,
                 disable_script_injection=False,
                 out_log_path=None):
  """Launches web page replay host.

  Args:
    wpr_archive_path: host sided WPR archive's path.
    record: Enables or disables WPR archive recording.
    network_condition_name: Network condition name available in
        emulation.NETWORK_CONDITIONS.
    disable_script_injection: Disable JavaScript file injections that is
      fighting against resources name entropy.
    out_log_path: Path of the WPR host's log.

  Returns:
    WprAttribute
  """
  if wpr_archive_path == None:
    _VerifySilentWprHost(record, network_condition_name)
    yield []
    return

  with common_util.TemporaryDirectory() as temp_home_dir:
    # Generate a root certification authority certificate for WPR.
    private_ca_cert_path = os.path.join(temp_home_dir, 'wpr.pem')
    ca_cert_path = os.path.join(temp_home_dir, 'wpr-cert.pem')
    certutils.write_dummy_ca_cert(*certutils.generate_dummy_ca_cert(),
                                  cert_path=private_ca_cert_path)
    assert os.path.isfile(ca_cert_path)
    certutils.install_cert_in_nssdb(temp_home_dir, ca_cert_path)

    with _WprHost(
        wpr_archive_path,
        record=record,
        network_condition_name=network_condition_name,
        disable_script_injection=disable_script_injection,
        wpr_ca_cert_path=private_ca_cert_path,
        out_log_path=out_log_path) as (http_port, https_port):
      chrome_args = _FormatWPRRelatedChromeArgumentFor(http_port, https_port)
      yield WprAttribute(chrome_args=chrome_args,
                         chrome_env_override={'HOME': temp_home_dir})


@contextlib.contextmanager
def RemoteWprHost(device, wpr_archive_path, record=False,
                  network_condition_name=None,
                  disable_script_injection=False,
                  out_log_path=None):
  """Launches web page replay host.

  Args:
    device: Android device.
    wpr_archive_path: host sided WPR archive's path.
    record: Enables or disables WPR archive recording.
    network_condition_name: Network condition name available in
        emulation.NETWORK_CONDITIONS.
    disable_script_injection: Disable JavaScript file injections that is
      fighting against resources name entropy.
    out_log_path: Path of the WPR host's log.

  Returns:
    WprAttribute
  """
  assert device
  if wpr_archive_path == None:
    _VerifySilentWprHost(record, network_condition_name)
    yield []
    return
  # Deploy certification authority to the device.
  temp_certificate_dir = tempfile.mkdtemp()
  wpr_ca_cert_path = os.path.join(temp_certificate_dir, 'testca.pem')
  certutils.write_dummy_ca_cert(*certutils.generate_dummy_ca_cert(),
                                cert_path=wpr_ca_cert_path)
  device_cert_util = adb_install_cert.AndroidCertInstaller(
      device.adb.GetDeviceSerial(), None, wpr_ca_cert_path,
      adb_wrapper.AdbWrapper.GetAdbPath())
  device_cert_util.install_cert(overwrite_cert=True)
  try:
    # Set up WPR server
    with _WprHost(
        wpr_archive_path,
        record=record,
        network_condition_name=network_condition_name,
        disable_script_injection=disable_script_injection,
        wpr_ca_cert_path=wpr_ca_cert_path,
        out_log_path=out_log_path) as (http_port, https_port):
      # Set up the forwarder.
      forwarder.Forwarder.Map([(0, http_port), (0, https_port)], device)
      device_http_port = forwarder.Forwarder.DevicePortForHostPort(http_port)
      device_https_port = forwarder.Forwarder.DevicePortForHostPort(https_port)
      try:
        chrome_args = _FormatWPRRelatedChromeArgumentFor(device_http_port,
                                                         device_https_port)
        yield WprAttribute(chrome_args=chrome_args, chrome_env_override={})
      finally:
        # Tear down the forwarder.
        forwarder.Forwarder.UnmapDevicePort(device_http_port, device)
        forwarder.Forwarder.UnmapDevicePort(device_https_port, device)
  finally:
    # Remove certification authority from the device.
    device_cert_util.remove_cert()
    shutil.rmtree(temp_certificate_dir)


# Deprecated
@contextlib.contextmanager
def _RemoteVideoRecorder(device, local_output_path, megabits_per_second):
  """Record a video on Device.

  Args:
    device: (device_utils.DeviceUtils) Android device to connect to.
    local_output_path: Output path were to save the video locally.
    megabits_per_second: Video recorder Mb/s.

  Yields:
    None
  """
  assert device
  if megabits_per_second > 100:
    raise ValueError('Android video capture cannot capture at %dmbps. '
                     'Max capture rate is 100mbps.' % megabits_per_second)
  assert local_output_path.endswith('.mp4')
  recorder = video_recorder.VideoRecorder(device, megabits_per_second)
  recorder.Start()
  try:
    yield
    recorder.Stop()
    recorder.Pull(host_file=local_output_path)
    recorder = None
  finally:
    if recorder:
      recorder.Stop()


@contextlib.contextmanager
def RemoteSpeedIndexRecorder(device, connection, local_output_path):
  """Records on a device a video compatible for speed-index computation.

  Note:
    Chrome should be opened with the --disable-infobars command line argument to
    avoid web page viewport size to be changed, that can change speed-index
    value.

  Args:
    device: (device_utils.DeviceUtils) Android device to connect to.
    connection: devtools connection.
    local_output_path: Output path were to save the video locally.

  Yields:
    None
  """
  # Paint the current HTML document with the ORANGE that video is detecting with
  # the view-port position and size.
  color = video.HIGHLIGHT_ORANGE_FRAME
  connection.ExecuteJavaScript("""
    (function() {
      var screen = document.createElement('div');
      screen.style.background = 'rgb(%d, %d, %d)';
      screen.style.position = 'fixed';
      screen.style.top = '0';
      screen.style.left = '0';
      screen.style.width = '100%%';
      screen.style.height = '100%%';
      screen.style.zIndex = '2147483638';
      document.body.appendChild(screen);
      requestAnimationFrame(function() {
        requestAnimationFrame(function() {
          window.__speedindex_screen = screen;
        });
      });
    })();
  """ % (color.r, color.g, color.b))
  connection.PollForJavaScriptExpression('!!window.__speedindex_screen', 1)

  with _RemoteVideoRecorder(device, local_output_path,
                            megabits_per_second=_SPEED_INDEX_VIDEO_BITRATE):
    # Paint the current HTML document with white so that it is not troubling the
    # speed index measurement.
    connection.ExecuteJavaScript("""
      (function() {
        requestAnimationFrame(function() {
          var screen = window.__speedindex_screen;
          screen.style.background = 'rgb(255, 255, 255)';
        });
      })();
    """)
    yield
