# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: rastervision/protos/keras_classification/pipeline.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from rastervision.protos.keras_classification import model_pb2 as rastervision_dot_protos_dot_keras__classification_dot_model__pb2
from rastervision.protos.keras_classification import trainer_pb2 as rastervision_dot_protos_dot_keras__classification_dot_trainer__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='rastervision/protos/keras_classification/pipeline.proto',
  package='keras_classification.protos',
  syntax='proto2',
  serialized_pb=_b('\n7rastervision/protos/keras_classification/pipeline.proto\x12\x1bkeras_classification.protos\x1a\x34rastervision/protos/keras_classification/model.proto\x1a\x36rastervision/protos/keras_classification/trainer.proto\"z\n\x0ePipelineConfig\x12\x31\n\x05model\x18\x01 \x02(\x0b\x32\".keras_classification.protos.Model\x12\x35\n\x07trainer\x18\x02 \x02(\x0b\x32$.keras_classification.protos.Trainer')
  ,
  dependencies=[rastervision_dot_protos_dot_keras__classification_dot_model__pb2.DESCRIPTOR,rastervision_dot_protos_dot_keras__classification_dot_trainer__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_PIPELINECONFIG = _descriptor.Descriptor(
  name='PipelineConfig',
  full_name='keras_classification.protos.PipelineConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='model', full_name='keras_classification.protos.PipelineConfig.model', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='trainer', full_name='keras_classification.protos.PipelineConfig.trainer', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=198,
  serialized_end=320,
)

_PIPELINECONFIG.fields_by_name['model'].message_type = rastervision_dot_protos_dot_keras__classification_dot_model__pb2._MODEL
_PIPELINECONFIG.fields_by_name['trainer'].message_type = rastervision_dot_protos_dot_keras__classification_dot_trainer__pb2._TRAINER
DESCRIPTOR.message_types_by_name['PipelineConfig'] = _PIPELINECONFIG

PipelineConfig = _reflection.GeneratedProtocolMessageType('PipelineConfig', (_message.Message,), dict(
  DESCRIPTOR = _PIPELINECONFIG,
  __module__ = 'rastervision.protos.keras_classification.pipeline_pb2'
  # @@protoc_insertion_point(class_scope:keras_classification.protos.PipelineConfig)
  ))
_sym_db.RegisterMessage(PipelineConfig)


# @@protoc_insertion_point(module_scope)