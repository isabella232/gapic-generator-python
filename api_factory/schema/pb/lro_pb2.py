# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/api/experimental/lro.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/api/experimental/lro.proto',
  package='google.api.experimental',
  syntax='proto3',
  serialized_pb=_b('\n!google/api/experimental/lro.proto\x12\x17google.api.experimental\x1a google/protobuf/descriptor.proto\"<\n\x0eOperationTypes\x12\x13\n\x0breturn_type\x18\x01 \x01(\t\x12\x15\n\rmetadata_type\x18\x02 \x01(\t:X\n\x05types\x12\x1e.google.protobuf.MethodOptions\x18\x80\x90\x03 \x01(\x0b\x32\'.google.api.experimental.OperationTypesb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_descriptor__pb2.DESCRIPTOR,])


TYPES_FIELD_NUMBER = 51200
types = _descriptor.FieldDescriptor(
  name='types', full_name='google.api.experimental.types', index=0,
  number=51200, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  options=None, file=DESCRIPTOR)


_OPERATIONTYPES = _descriptor.Descriptor(
  name='OperationTypes',
  full_name='google.api.experimental.OperationTypes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='return_type', full_name='google.api.experimental.OperationTypes.return_type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='metadata_type', full_name='google.api.experimental.OperationTypes.metadata_type', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=96,
  serialized_end=156,
)

DESCRIPTOR.message_types_by_name['OperationTypes'] = _OPERATIONTYPES
DESCRIPTOR.extensions_by_name['types'] = types
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

OperationTypes = _reflection.GeneratedProtocolMessageType('OperationTypes', (_message.Message,), dict(
  DESCRIPTOR = _OPERATIONTYPES,
  __module__ = 'google.api.experimental.lro_pb2'
  # @@protoc_insertion_point(class_scope:google.api.experimental.OperationTypes)
  ))
_sym_db.RegisterMessage(OperationTypes)

types.message_type = _OPERATIONTYPES
google_dot_protobuf_dot_descriptor__pb2.MethodOptions.RegisterExtension(types)

# @@protoc_insertion_point(module_scope)
