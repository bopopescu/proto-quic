# Copyright 2016 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

import base64
import json
import uuid

class ClovisTask(object):
  """Generic task, generated by the AppEngine frontend and consumed by the
  ComputeEngine backend.
  """

  def __init__(self, action, action_params, backend_params):
    """ See tools/android/loading/cloud/frontend/README.md for a specification
    of the parameters.

    Args:
      action(str): Action accomplished by this task.
      action_params(dict): Parameters of task.
      backend_params(dict): Parameters of the instances running the task.
          If this is None, no instances are created. If this dictionary has no
          'tag' key, a unique tag will be generated.
    """
    self._action = action
    self._action_params = action_params or {}
    self._backend_params = backend_params or {}
    # If no tag is specified, generate a unique tag.
    if not self._backend_params.get('tag'):
      self._backend_params.update({'tag': str(uuid.uuid1())})

  @classmethod
  def FromJsonDict(cls, json_dict):
    """Loads a ClovisTask from a JSON dictionary.

    Returns:
      ClovisTask: The task, or None if the string is invalid.
    """
    try:
      action = json_dict['action']
      action_params = json_dict['action_params']
      # Vaidate the format.
      if action == 'trace':
        urls = action_params['urls']
        if (type(urls) is not list) or (len(urls) == 0):
          return None
      elif action == 'report':
        if not action_params.get('trace_bucket'):
          return None
      else:
        # When more actions are supported, check that they are valid here.
        return None
      return cls(action, action_params, json_dict.get('backend_params'))
    except Exception:
      return None

  @classmethod
  def FromJsonString(cls, json_string):
    """Loads a ClovisTask from a JSON string.

    Returns:
      ClovisTask: The task, or None if the string is invalid.
    """
    try:
      return cls.FromJsonDict(json.loads(json_string))
    except Exception:
      return None

  @classmethod
  def FromBase64(cls, base64_string):
    """Loads a ClovisTask from a base 64 string."""
    return ClovisTask.FromJsonString(base64.b64decode(base64_string))

  def ToJsonDict(self):
    """Returns the JSON representation of the task as a dictionary."""
    return {'action': self._action, 'action_params': self._action_params,
            'backend_params': self._backend_params}

  def ToJsonString(self):
    """Returns the JSON representation of the task as a string."""
    return json.dumps(self.ToJsonDict())

  def Action(self):
    return self._action

  def ActionParams(self):
    return self._action_params

  def BackendParams(self):
    return self._backend_params

