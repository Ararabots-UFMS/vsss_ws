# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: packet.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import sim_cam.sim.command_pb2 as command__pb2
import sim_cam.sim.replacement_pb2 as replacement__pb2
import sim_cam.sim.common_pb2 as common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='packet.proto',
  package='fira_message.sim_to_ref',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0cpacket.proto\x12\x17\x66ira_message.sim_to_ref\x1a\rcommand.proto\x1a\x11replacement.proto\x1a\x0c\x63ommon.proto\"o\n\x06Packet\x12.\n\x03\x63md\x18\x01 \x01(\x0b\x32!.fira_message.sim_to_ref.Commands\x12\x35\n\x07replace\x18\x02 \x01(\x0b\x32$.fira_message.sim_to_ref.Replacement\"\x8d\x01\n\x0b\x45nvironment\x12\x0c\n\x04step\x18\x01 \x01(\r\x12\"\n\x05\x66rame\x18\x02 \x01(\x0b\x32\x13.fira_message.Frame\x12\"\n\x05\x66ield\x18\x03 \x01(\x0b\x32\x13.fira_message.Field\x12\x12\n\ngoals_blue\x18\x04 \x01(\r\x12\x14\n\x0cgoals_yellow\x18\x05 \x01(\r2_\n\x08Simulate\x12S\n\x08Simulate\x12\x1f.fira_message.sim_to_ref.Packet\x1a$.fira_message.sim_to_ref.Environment\"\x00\x62\x06proto3')
  ,
  dependencies=[command__pb2.DESCRIPTOR,replacement__pb2.DESCRIPTOR,common__pb2.DESCRIPTOR,])




_PACKET = _descriptor.Descriptor(
  name='Packet',
  full_name='fira_message.sim_to_ref.Packet',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cmd', full_name='fira_message.sim_to_ref.Packet.cmd', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='replace', full_name='fira_message.sim_to_ref.Packet.replace', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=89,
  serialized_end=200,
)


_ENVIRONMENT = _descriptor.Descriptor(
  name='Environment',
  full_name='fira_message.sim_to_ref.Environment',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='step', full_name='fira_message.sim_to_ref.Environment.step', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='frame', full_name='fira_message.sim_to_ref.Environment.frame', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='field', full_name='fira_message.sim_to_ref.Environment.field', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='goals_blue', full_name='fira_message.sim_to_ref.Environment.goals_blue', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='goals_yellow', full_name='fira_message.sim_to_ref.Environment.goals_yellow', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=203,
  serialized_end=344,
)

_PACKET.fields_by_name['cmd'].message_type = command__pb2._COMMANDS
_PACKET.fields_by_name['replace'].message_type = replacement__pb2._REPLACEMENT
_ENVIRONMENT.fields_by_name['frame'].message_type = common__pb2._FRAME
_ENVIRONMENT.fields_by_name['field'].message_type = common__pb2._FIELD
DESCRIPTOR.message_types_by_name['Packet'] = _PACKET
DESCRIPTOR.message_types_by_name['Environment'] = _ENVIRONMENT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Packet = _reflection.GeneratedProtocolMessageType('Packet', (_message.Message,), dict(
  DESCRIPTOR = _PACKET,
  __module__ = 'packet_pb2'
  # @@protoc_insertion_point(class_scope:fira_message.sim_to_ref.Packet)
  ))
_sym_db.RegisterMessage(Packet)

Environment = _reflection.GeneratedProtocolMessageType('Environment', (_message.Message,), dict(
  DESCRIPTOR = _ENVIRONMENT,
  __module__ = 'packet_pb2'
  # @@protoc_insertion_point(class_scope:fira_message.sim_to_ref.Environment)
  ))
_sym_db.RegisterMessage(Environment)



_SIMULATE = _descriptor.ServiceDescriptor(
  name='Simulate',
  full_name='fira_message.sim_to_ref.Simulate',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=346,
  serialized_end=441,
  methods=[
  _descriptor.MethodDescriptor(
    name='Simulate',
    full_name='fira_message.sim_to_ref.Simulate.Simulate',
    index=0,
    containing_service=None,
    input_type=_PACKET,
    output_type=_ENVIRONMENT,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_SIMULATE)

DESCRIPTOR.services_by_name['Simulate'] = _SIMULATE

# @@protoc_insertion_point(module_scope)
