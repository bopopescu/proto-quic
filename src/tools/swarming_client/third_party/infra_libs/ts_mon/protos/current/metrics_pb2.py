# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: metrics.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import acquisition_network_device_pb2
import acquisition_task_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='metrics.proto',
  package='ts_mon.proto',
  serialized_pb=_b('\n\rmetrics.proto\x12\x0cts_mon.proto\x1a acquisition_network_device.proto\x1a\x16\x61\x63quisition_task.proto\"u\n\x11MetricsCollection\x12\'\n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32\x19.ts_mon.proto.MetricsData\x12\x1a\n\x12start_timestamp_us\x18\x02 \x01(\x04\x12\x1b\n\x13\x63ollection_point_id\x18\x03 \x01(\t\"\xc1\x01\n\x0cMetricsField\x12\x0c\n\x04name\x18\x01 \x01(\t\x12:\n\x04type\x18\x03 \x01(\x0e\x32$.ts_mon.proto.MetricsField.FieldType:\x06STRING\x12\x14\n\x0cstring_value\x18\x04 \x01(\t\x12\x11\n\tint_value\x18\x05 \x01(\x03\x12\x12\n\nbool_value\x18\x06 \x01(\x08\"*\n\tFieldType\x12\n\n\x06STRING\x10\x01\x12\x07\n\x03INT\x10\x02\x12\x08\n\x04\x42OOL\x10\x03\"\xcf\x03\n\x17PrecomputedDistribution\x12\x41\n\tspec_type\x18\x01 \x01(\x0e\x32..ts_mon.proto.PrecomputedDistribution.SpecType\x12\x11\n\x05width\x18\x02 \x01(\x01:\x02\x31\x30\x12\x18\n\rgrowth_factor\x18\x03 \x01(\x01:\x01\x30\x12\x17\n\x0bnum_buckets\x18\x04 \x01(\x05:\x02\x31\x30\x12\x14\n\x0clower_bounds\x18\x05 \x03(\x01\x12\x1c\n\ris_cumulative\x18\x06 \x01(\x08:\x05\x66\x61lse\x12\x0e\n\x06\x62ucket\x18\x07 \x03(\x12\x12\x11\n\tunderflow\x18\x08 \x01(\x12\x12\x10\n\x08overflow\x18\t \x01(\x12\x12\x0c\n\x04mean\x18\n \x01(\x01\x12 \n\x18sum_of_squared_deviation\x18\x0b \x01(\x01\"\x91\x01\n\x08SpecType\x12\x19\n\x15\x43\x41NONICAL_POWERS_OF_2\x10\x01\x12 \n\x1c\x43\x41NONICAL_POWERS_OF_10_P_0_2\x10\x02\x12\x1a\n\x16\x43\x41NONICAL_POWERS_OF_10\x10\x03\x12\x18\n\x14\x43USTOM_PARAMETERIZED\x10\x14\x12\x12\n\x0e\x43USTOM_BOUNDED\x10\x15\"\xe6\x05\n\x0bMetricsData\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\x1a\n\x12metric_name_prefix\x18\x02 \x01(\t\x12\x33\n\x0enetwork_device\x18\x0b \x01(\x0b\x32\x1b.ts_mon.proto.NetworkDevice\x12 \n\x04task\x18\x0c \x01(\x0b\x32\x12.ts_mon.proto.Task\x12*\n\x06\x66ields\x18\x14 \x03(\x0b\x32\x1a.ts_mon.proto.MetricsField\x12\x0f\n\x07\x63ounter\x18\x1e \x01(\x03\x12\r\n\x05gauge\x18  \x01(\x03\x12\"\n\x1anoncumulative_double_value\x18\" \x01(\x01\x12;\n\x0c\x64istribution\x18# \x01(\x0b\x32%.ts_mon.proto.PrecomputedDistribution\x12\x14\n\x0cstring_value\x18$ \x01(\t\x12\x15\n\rboolean_value\x18% \x01(\x08\x12\x1f\n\x17\x63umulative_double_value\x18& \x01(\x01\x12\x1a\n\x12start_timestamp_us\x18( \x01(\x04\x12.\n\x05units\x18) \x01(\x0e\x32\x1f.ts_mon.proto.MetricsData.Units\x12\x13\n\x0b\x64\x65scription\x18+ \x01(\t\"\xf9\x01\n\x05Units\x12\x11\n\rUNKNOWN_UNITS\x10\x00\x12\x0b\n\x07SECONDS\x10\x01\x12\x10\n\x0cMILLISECONDS\x10\x02\x12\x10\n\x0cMICROSECONDS\x10\x03\x12\x0f\n\x0bNANOSECONDS\x10\x04\x12\x08\n\x04\x42ITS\x10\x15\x12\t\n\x05\x42YTES\x10\x16\x12\r\n\tKILOBYTES\x10\x1f\x12\r\n\tMEGABYTES\x10 \x12\r\n\tGIGABYTES\x10!\x12\r\n\tKIBIBYTES\x10)\x12\r\n\tMEBIBYTES\x10*\x12\r\n\tGIBIBYTES\x10+\x12\x08\n\x04\x41MPS\x10<\x12\r\n\tMILLIAMPS\x10=\x12\x13\n\x0f\x44\x45GREES_CELSIUS\x10>')
  ,
  dependencies=[acquisition_network_device_pb2.DESCRIPTOR,acquisition_task_pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_METRICSFIELD_FIELDTYPE = _descriptor.EnumDescriptor(
  name='FieldType',
  full_name='ts_mon.proto.MetricsField.FieldType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='STRING', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INT', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BOOL', index=2, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=360,
  serialized_end=402,
)
_sym_db.RegisterEnumDescriptor(_METRICSFIELD_FIELDTYPE)

_PRECOMPUTEDDISTRIBUTION_SPECTYPE = _descriptor.EnumDescriptor(
  name='SpecType',
  full_name='ts_mon.proto.PrecomputedDistribution.SpecType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='CANONICAL_POWERS_OF_2', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CANONICAL_POWERS_OF_10_P_0_2', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CANONICAL_POWERS_OF_10', index=2, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CUSTOM_PARAMETERIZED', index=3, number=20,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CUSTOM_BOUNDED', index=4, number=21,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=723,
  serialized_end=868,
)
_sym_db.RegisterEnumDescriptor(_PRECOMPUTEDDISTRIBUTION_SPECTYPE)

_METRICSDATA_UNITS = _descriptor.EnumDescriptor(
  name='Units',
  full_name='ts_mon.proto.MetricsData.Units',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN_UNITS', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SECONDS', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MILLISECONDS', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MICROSECONDS', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NANOSECONDS', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BITS', index=5, number=21,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BYTES', index=6, number=22,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='KILOBYTES', index=7, number=31,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MEGABYTES', index=8, number=32,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GIGABYTES', index=9, number=33,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='KIBIBYTES', index=10, number=41,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MEBIBYTES', index=11, number=42,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GIBIBYTES', index=12, number=43,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AMPS', index=13, number=60,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MILLIAMPS', index=14, number=61,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DEGREES_CELSIUS', index=15, number=62,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1364,
  serialized_end=1613,
)
_sym_db.RegisterEnumDescriptor(_METRICSDATA_UNITS)


_METRICSCOLLECTION = _descriptor.Descriptor(
  name='MetricsCollection',
  full_name='ts_mon.proto.MetricsCollection',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='ts_mon.proto.MetricsCollection.data', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='start_timestamp_us', full_name='ts_mon.proto.MetricsCollection.start_timestamp_us', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='collection_point_id', full_name='ts_mon.proto.MetricsCollection.collection_point_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=89,
  serialized_end=206,
)


_METRICSFIELD = _descriptor.Descriptor(
  name='MetricsField',
  full_name='ts_mon.proto.MetricsField',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='ts_mon.proto.MetricsField.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='ts_mon.proto.MetricsField.type', index=1,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='string_value', full_name='ts_mon.proto.MetricsField.string_value', index=2,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='int_value', full_name='ts_mon.proto.MetricsField.int_value', index=3,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bool_value', full_name='ts_mon.proto.MetricsField.bool_value', index=4,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _METRICSFIELD_FIELDTYPE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=209,
  serialized_end=402,
)


_PRECOMPUTEDDISTRIBUTION = _descriptor.Descriptor(
  name='PrecomputedDistribution',
  full_name='ts_mon.proto.PrecomputedDistribution',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='spec_type', full_name='ts_mon.proto.PrecomputedDistribution.spec_type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='width', full_name='ts_mon.proto.PrecomputedDistribution.width', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=10,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='growth_factor', full_name='ts_mon.proto.PrecomputedDistribution.growth_factor', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_buckets', full_name='ts_mon.proto.PrecomputedDistribution.num_buckets', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=10,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lower_bounds', full_name='ts_mon.proto.PrecomputedDistribution.lower_bounds', index=4,
      number=5, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='is_cumulative', full_name='ts_mon.proto.PrecomputedDistribution.is_cumulative', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bucket', full_name='ts_mon.proto.PrecomputedDistribution.bucket', index=6,
      number=7, type=18, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='underflow', full_name='ts_mon.proto.PrecomputedDistribution.underflow', index=7,
      number=8, type=18, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='overflow', full_name='ts_mon.proto.PrecomputedDistribution.overflow', index=8,
      number=9, type=18, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mean', full_name='ts_mon.proto.PrecomputedDistribution.mean', index=9,
      number=10, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sum_of_squared_deviation', full_name='ts_mon.proto.PrecomputedDistribution.sum_of_squared_deviation', index=10,
      number=11, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _PRECOMPUTEDDISTRIBUTION_SPECTYPE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=405,
  serialized_end=868,
)


_METRICSDATA = _descriptor.Descriptor(
  name='MetricsData',
  full_name='ts_mon.proto.MetricsData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='ts_mon.proto.MetricsData.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='metric_name_prefix', full_name='ts_mon.proto.MetricsData.metric_name_prefix', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='network_device', full_name='ts_mon.proto.MetricsData.network_device', index=2,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='task', full_name='ts_mon.proto.MetricsData.task', index=3,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fields', full_name='ts_mon.proto.MetricsData.fields', index=4,
      number=20, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='counter', full_name='ts_mon.proto.MetricsData.counter', index=5,
      number=30, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gauge', full_name='ts_mon.proto.MetricsData.gauge', index=6,
      number=32, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='noncumulative_double_value', full_name='ts_mon.proto.MetricsData.noncumulative_double_value', index=7,
      number=34, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='distribution', full_name='ts_mon.proto.MetricsData.distribution', index=8,
      number=35, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='string_value', full_name='ts_mon.proto.MetricsData.string_value', index=9,
      number=36, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='boolean_value', full_name='ts_mon.proto.MetricsData.boolean_value', index=10,
      number=37, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cumulative_double_value', full_name='ts_mon.proto.MetricsData.cumulative_double_value', index=11,
      number=38, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='start_timestamp_us', full_name='ts_mon.proto.MetricsData.start_timestamp_us', index=12,
      number=40, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='units', full_name='ts_mon.proto.MetricsData.units', index=13,
      number=41, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='description', full_name='ts_mon.proto.MetricsData.description', index=14,
      number=43, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _METRICSDATA_UNITS,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=871,
  serialized_end=1613,
)

_METRICSCOLLECTION.fields_by_name['data'].message_type = _METRICSDATA
_METRICSFIELD.fields_by_name['type'].enum_type = _METRICSFIELD_FIELDTYPE
_METRICSFIELD_FIELDTYPE.containing_type = _METRICSFIELD
_PRECOMPUTEDDISTRIBUTION.fields_by_name['spec_type'].enum_type = _PRECOMPUTEDDISTRIBUTION_SPECTYPE
_PRECOMPUTEDDISTRIBUTION_SPECTYPE.containing_type = _PRECOMPUTEDDISTRIBUTION
_METRICSDATA.fields_by_name['network_device'].message_type = acquisition_network_device_pb2._NETWORKDEVICE
_METRICSDATA.fields_by_name['task'].message_type = acquisition_task_pb2._TASK
_METRICSDATA.fields_by_name['fields'].message_type = _METRICSFIELD
_METRICSDATA.fields_by_name['distribution'].message_type = _PRECOMPUTEDDISTRIBUTION
_METRICSDATA.fields_by_name['units'].enum_type = _METRICSDATA_UNITS
_METRICSDATA_UNITS.containing_type = _METRICSDATA
DESCRIPTOR.message_types_by_name['MetricsCollection'] = _METRICSCOLLECTION
DESCRIPTOR.message_types_by_name['MetricsField'] = _METRICSFIELD
DESCRIPTOR.message_types_by_name['PrecomputedDistribution'] = _PRECOMPUTEDDISTRIBUTION
DESCRIPTOR.message_types_by_name['MetricsData'] = _METRICSDATA

MetricsCollection = _reflection.GeneratedProtocolMessageType('MetricsCollection', (_message.Message,), dict(
  DESCRIPTOR = _METRICSCOLLECTION,
  __module__ = 'metrics_pb2'
  # @@protoc_insertion_point(class_scope:ts_mon.proto.MetricsCollection)
  ))
_sym_db.RegisterMessage(MetricsCollection)

MetricsField = _reflection.GeneratedProtocolMessageType('MetricsField', (_message.Message,), dict(
  DESCRIPTOR = _METRICSFIELD,
  __module__ = 'metrics_pb2'
  # @@protoc_insertion_point(class_scope:ts_mon.proto.MetricsField)
  ))
_sym_db.RegisterMessage(MetricsField)

PrecomputedDistribution = _reflection.GeneratedProtocolMessageType('PrecomputedDistribution', (_message.Message,), dict(
  DESCRIPTOR = _PRECOMPUTEDDISTRIBUTION,
  __module__ = 'metrics_pb2'
  # @@protoc_insertion_point(class_scope:ts_mon.proto.PrecomputedDistribution)
  ))
_sym_db.RegisterMessage(PrecomputedDistribution)

MetricsData = _reflection.GeneratedProtocolMessageType('MetricsData', (_message.Message,), dict(
  DESCRIPTOR = _METRICSDATA,
  __module__ = 'metrics_pb2'
  # @@protoc_insertion_point(class_scope:ts_mon.proto.MetricsData)
  ))
_sym_db.RegisterMessage(MetricsData)


# @@protoc_insertion_point(module_scope)
