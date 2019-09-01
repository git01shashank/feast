# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from feast.serving import ServingService_pb2 as feast_dot_serving_dot_ServingService__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


class ServingServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetFeastServingVersion = channel.unary_unary(
        '/feast.serving.ServingService/GetFeastServingVersion',
        request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        response_deserializer=feast_dot_serving_dot_ServingService__pb2.GetFeastServingVersionResponse.FromString,
        )
    self.GetFeastServingType = channel.unary_unary(
        '/feast.serving.ServingService/GetFeastServingType',
        request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        response_deserializer=feast_dot_serving_dot_ServingService__pb2.GetFeastServingTypeResponse.FromString,
        )
    self.GetOnlineFeatures = channel.unary_unary(
        '/feast.serving.ServingService/GetOnlineFeatures',
        request_serializer=feast_dot_serving_dot_ServingService__pb2.GetFeaturesRequest.SerializeToString,
        response_deserializer=feast_dot_serving_dot_ServingService__pb2.GetOnlineFeaturesResponse.FromString,
        )
    self.GetBatchFeatures = channel.unary_unary(
        '/feast.serving.ServingService/GetBatchFeatures',
        request_serializer=feast_dot_serving_dot_ServingService__pb2.GetFeaturesRequest.SerializeToString,
        response_deserializer=feast_dot_serving_dot_ServingService__pb2.GetBatchFeaturesResponse.FromString,
        )
    self.GetBatchFeaturesJobStatus = channel.unary_unary(
        '/feast.serving.ServingService/GetBatchFeaturesJobStatus',
        request_serializer=feast_dot_serving_dot_ServingService__pb2.BatchFeaturesJob.GetStatusRequest.SerializeToString,
        response_deserializer=feast_dot_serving_dot_ServingService__pb2.BatchFeaturesJob.GetStatusResponse.FromString,
        )
    self.GetBatchFeaturesJobUploadUrl = channel.unary_unary(
        '/feast.serving.ServingService/GetBatchFeaturesJobUploadUrl',
        request_serializer=feast_dot_serving_dot_ServingService__pb2.BatchFeaturesJob.GetUploadUrlRequest.SerializeToString,
        response_deserializer=feast_dot_serving_dot_ServingService__pb2.BatchFeaturesJob.GetUploadUrlResponse.FromString,
        )
    self.SetBatchFeaturesJobUploadComplete = channel.unary_unary(
        '/feast.serving.ServingService/SetBatchFeaturesJobUploadComplete',
        request_serializer=feast_dot_serving_dot_ServingService__pb2.BatchFeaturesJob.SetUploadCompleteRequest.SerializeToString,
        response_deserializer=feast_dot_serving_dot_ServingService__pb2.BatchFeaturesJob.SetUploadCompleteResponse.FromString,
        )


class ServingServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def GetFeastServingVersion(self, request, context):
    """Retrieve version information about this Feast deployment
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetFeastServingType(self, request, context):
    """Get Feast serving storage type (online or batch)
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetOnlineFeatures(self, request, context):
    """Get online features from Feast serving. This is a synchronous response.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetBatchFeatures(self, request, context):
    """Get batch features from Feast serving. This is an async job.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetBatchFeaturesJobStatus(self, request, context):
    """Get the current status of a batch feature request job
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetBatchFeaturesJobUploadUrl(self, request, context):
    """Request a signed URL where a Feast client can upload user entity data
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SetBatchFeaturesJobUploadComplete(self, request, context):
    """Set the state of the batch feature job to complete after user entity data has been uploaded
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ServingServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetFeastServingVersion': grpc.unary_unary_rpc_method_handler(
          servicer.GetFeastServingVersion,
          request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
          response_serializer=feast_dot_serving_dot_ServingService__pb2.GetFeastServingVersionResponse.SerializeToString,
      ),
      'GetFeastServingType': grpc.unary_unary_rpc_method_handler(
          servicer.GetFeastServingType,
          request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
          response_serializer=feast_dot_serving_dot_ServingService__pb2.GetFeastServingTypeResponse.SerializeToString,
      ),
      'GetOnlineFeatures': grpc.unary_unary_rpc_method_handler(
          servicer.GetOnlineFeatures,
          request_deserializer=feast_dot_serving_dot_ServingService__pb2.GetFeaturesRequest.FromString,
          response_serializer=feast_dot_serving_dot_ServingService__pb2.GetOnlineFeaturesResponse.SerializeToString,
      ),
      'GetBatchFeatures': grpc.unary_unary_rpc_method_handler(
          servicer.GetBatchFeatures,
          request_deserializer=feast_dot_serving_dot_ServingService__pb2.GetFeaturesRequest.FromString,
          response_serializer=feast_dot_serving_dot_ServingService__pb2.GetBatchFeaturesResponse.SerializeToString,
      ),
      'GetBatchFeaturesJobStatus': grpc.unary_unary_rpc_method_handler(
          servicer.GetBatchFeaturesJobStatus,
          request_deserializer=feast_dot_serving_dot_ServingService__pb2.BatchFeaturesJob.GetStatusRequest.FromString,
          response_serializer=feast_dot_serving_dot_ServingService__pb2.BatchFeaturesJob.GetStatusResponse.SerializeToString,
      ),
      'GetBatchFeaturesJobUploadUrl': grpc.unary_unary_rpc_method_handler(
          servicer.GetBatchFeaturesJobUploadUrl,
          request_deserializer=feast_dot_serving_dot_ServingService__pb2.BatchFeaturesJob.GetUploadUrlRequest.FromString,
          response_serializer=feast_dot_serving_dot_ServingService__pb2.BatchFeaturesJob.GetUploadUrlResponse.SerializeToString,
      ),
      'SetBatchFeaturesJobUploadComplete': grpc.unary_unary_rpc_method_handler(
          servicer.SetBatchFeaturesJobUploadComplete,
          request_deserializer=feast_dot_serving_dot_ServingService__pb2.BatchFeaturesJob.SetUploadCompleteRequest.FromString,
          response_serializer=feast_dot_serving_dot_ServingService__pb2.BatchFeaturesJob.SetUploadCompleteResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'feast.serving.ServingService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
