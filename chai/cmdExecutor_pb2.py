# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chai/cmdExecutor.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16\x63hai/cmdExecutor.proto\x12\x04shai\"4\n\nCmdRequest\x12\x16\n\x03\x63md\x18\x01 \x01(\x0e\x32\t.shai.Cmd\x12\x0e\n\x06\x63onfig\x18\x02 \x01(\t\"=\n\x0b\x43mdResponse\x12\x11\n\x07success\x18\x01 \x01(\tH\x00\x12\x11\n\x07\x66\x61ilure\x18\x02 \x01(\tH\x00\x42\x08\n\x06result**\n\x03\x43md\x12\t\n\x05PARSE\x10\x00\x12\t\n\x05\x43HECK\x10\x01\x12\r\n\tTYPECHECK\x10\x03\x32\x39\n\x0b\x43mdExecutor\x12*\n\x03run\x12\x10.shai.CmdRequest\x1a\x11.shai.CmdResponseB7\n\x1b\x61t.forsyte.apalache.shai.v1B\x10\x43mdExecutorProtoP\x01\xa2\x02\x03TEPb\x06proto3')

_CMD = DESCRIPTOR.enum_types_by_name['Cmd']
Cmd = enum_type_wrapper.EnumTypeWrapper(_CMD)
PARSE = 0
CHECK = 1
TYPECHECK = 3


_CMDREQUEST = DESCRIPTOR.message_types_by_name['CmdRequest']
_CMDRESPONSE = DESCRIPTOR.message_types_by_name['CmdResponse']
CmdRequest = _reflection.GeneratedProtocolMessageType('CmdRequest', (_message.Message,), {
  'DESCRIPTOR' : _CMDREQUEST,
  '__module__' : 'chai.cmdExecutor_pb2'
  # @@protoc_insertion_point(class_scope:shai.CmdRequest)
  })
_sym_db.RegisterMessage(CmdRequest)

CmdResponse = _reflection.GeneratedProtocolMessageType('CmdResponse', (_message.Message,), {
  'DESCRIPTOR' : _CMDRESPONSE,
  '__module__' : 'chai.cmdExecutor_pb2'
  # @@protoc_insertion_point(class_scope:shai.CmdResponse)
  })
_sym_db.RegisterMessage(CmdResponse)

_CMDEXECUTOR = DESCRIPTOR.services_by_name['CmdExecutor']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\033at.forsyte.apalache.shai.v1B\020CmdExecutorProtoP\001\242\002\003TEP'
  _CMD._serialized_start=149
  _CMD._serialized_end=191
  _CMDREQUEST._serialized_start=32
  _CMDREQUEST._serialized_end=84
  _CMDRESPONSE._serialized_start=86
  _CMDRESPONSE._serialized_end=147
  _CMDEXECUTOR._serialized_start=193
  _CMDEXECUTOR._serialized_end=250
# @@protoc_insertion_point(module_scope)