# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chai/transExplorer.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18\x63hai/transExplorer.proto\x12\x12shai.transExplorer\"\r\n\x0bPingRequest\"\x0e\n\x0cPongResponse\"\x10\n\x0e\x43onnectRequest\"\x18\n\nConnection\x12\n\n\x02id\x18\x01 \x01(\t\"[\n\x10LoadModelRequest\x12,\n\x04\x63onn\x18\x01 \x01(\x0b\x32\x1e.shai.transExplorer.Connection\x12\x0c\n\x04spec\x18\x02 \x01(\t\x12\x0b\n\x03\x61ux\x18\x03 \x03(\t\"a\n\x12TransExplorerError\x12=\n\terrorType\x18\x01 \x01(\x0e\x32*.shai.transExplorer.TransExplorerErrorType\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\t\"d\n\x11LoadModelResponse\x12\x0e\n\x04spec\x18\x01 \x01(\tH\x00\x12\x35\n\x03\x65rr\x18\x02 \x01(\x0b\x32&.shai.transExplorer.TransExplorerErrorH\x00\x42\x08\n\x06result*:\n\x16TransExplorerErrorType\x12\x10\n\x0cPASS_FAILURE\x10\x00\x12\x0e\n\nUNEXPECTED\x10\x01\x32\x8a\x02\n\rTransExplorer\x12T\n\x0eopenConnection\x12\".shai.transExplorer.ConnectRequest\x1a\x1e.shai.transExplorer.Connection\x12X\n\tloadModel\x12$.shai.transExplorer.LoadModelRequest\x1a%.shai.transExplorer.LoadModelResponse\x12I\n\x04ping\x12\x1f.shai.transExplorer.PingRequest\x1a .shai.transExplorer.PongResponseB3\n\x1b\x61t.forsyte.apalache.shai.v1B\x12TransExplorerProtoP\x01\x62\x06proto3')

_TRANSEXPLORERERRORTYPE = DESCRIPTOR.enum_types_by_name['TransExplorerErrorType']
TransExplorerErrorType = enum_type_wrapper.EnumTypeWrapper(_TRANSEXPLORERERRORTYPE)
PASS_FAILURE = 0
UNEXPECTED = 1


_PINGREQUEST = DESCRIPTOR.message_types_by_name['PingRequest']
_PONGRESPONSE = DESCRIPTOR.message_types_by_name['PongResponse']
_CONNECTREQUEST = DESCRIPTOR.message_types_by_name['ConnectRequest']
_CONNECTION = DESCRIPTOR.message_types_by_name['Connection']
_LOADMODELREQUEST = DESCRIPTOR.message_types_by_name['LoadModelRequest']
_TRANSEXPLORERERROR = DESCRIPTOR.message_types_by_name['TransExplorerError']
_LOADMODELRESPONSE = DESCRIPTOR.message_types_by_name['LoadModelResponse']
PingRequest = _reflection.GeneratedProtocolMessageType('PingRequest', (_message.Message,), {
  'DESCRIPTOR' : _PINGREQUEST,
  '__module__' : 'chai.transExplorer_pb2'
  # @@protoc_insertion_point(class_scope:shai.transExplorer.PingRequest)
  })
_sym_db.RegisterMessage(PingRequest)

PongResponse = _reflection.GeneratedProtocolMessageType('PongResponse', (_message.Message,), {
  'DESCRIPTOR' : _PONGRESPONSE,
  '__module__' : 'chai.transExplorer_pb2'
  # @@protoc_insertion_point(class_scope:shai.transExplorer.PongResponse)
  })
_sym_db.RegisterMessage(PongResponse)

ConnectRequest = _reflection.GeneratedProtocolMessageType('ConnectRequest', (_message.Message,), {
  'DESCRIPTOR' : _CONNECTREQUEST,
  '__module__' : 'chai.transExplorer_pb2'
  # @@protoc_insertion_point(class_scope:shai.transExplorer.ConnectRequest)
  })
_sym_db.RegisterMessage(ConnectRequest)

Connection = _reflection.GeneratedProtocolMessageType('Connection', (_message.Message,), {
  'DESCRIPTOR' : _CONNECTION,
  '__module__' : 'chai.transExplorer_pb2'
  # @@protoc_insertion_point(class_scope:shai.transExplorer.Connection)
  })
_sym_db.RegisterMessage(Connection)

LoadModelRequest = _reflection.GeneratedProtocolMessageType('LoadModelRequest', (_message.Message,), {
  'DESCRIPTOR' : _LOADMODELREQUEST,
  '__module__' : 'chai.transExplorer_pb2'
  # @@protoc_insertion_point(class_scope:shai.transExplorer.LoadModelRequest)
  })
_sym_db.RegisterMessage(LoadModelRequest)

TransExplorerError = _reflection.GeneratedProtocolMessageType('TransExplorerError', (_message.Message,), {
  'DESCRIPTOR' : _TRANSEXPLORERERROR,
  '__module__' : 'chai.transExplorer_pb2'
  # @@protoc_insertion_point(class_scope:shai.transExplorer.TransExplorerError)
  })
_sym_db.RegisterMessage(TransExplorerError)

LoadModelResponse = _reflection.GeneratedProtocolMessageType('LoadModelResponse', (_message.Message,), {
  'DESCRIPTOR' : _LOADMODELRESPONSE,
  '__module__' : 'chai.transExplorer_pb2'
  # @@protoc_insertion_point(class_scope:shai.transExplorer.LoadModelResponse)
  })
_sym_db.RegisterMessage(LoadModelResponse)

_TRANSEXPLORER = DESCRIPTOR.services_by_name['TransExplorer']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\033at.forsyte.apalache.shai.v1B\022TransExplorerProtoP\001'
  _TRANSEXPLORERERRORTYPE._serialized_start=417
  _TRANSEXPLORERERRORTYPE._serialized_end=475
  _PINGREQUEST._serialized_start=48
  _PINGREQUEST._serialized_end=61
  _PONGRESPONSE._serialized_start=63
  _PONGRESPONSE._serialized_end=77
  _CONNECTREQUEST._serialized_start=79
  _CONNECTREQUEST._serialized_end=95
  _CONNECTION._serialized_start=97
  _CONNECTION._serialized_end=121
  _LOADMODELREQUEST._serialized_start=123
  _LOADMODELREQUEST._serialized_end=214
  _TRANSEXPLORERERROR._serialized_start=216
  _TRANSEXPLORERERROR._serialized_end=313
  _LOADMODELRESPONSE._serialized_start=315
  _LOADMODELRESPONSE._serialized_end=415
  _TRANSEXPLORER._serialized_start=478
  _TRANSEXPLORER._serialized_end=744
# @@protoc_insertion_point(module_scope)
