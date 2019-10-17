# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities

import isolate_bot_pb2 as isolate__bot__pb2


class FileServiceStub(object):
  """FileService exposes the main operations of an Isolate server
  to upload and download blobs.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Contains = channel.unary_unary(
        '/luci.swarming.bot.FileService/Contains',
        request_serializer=isolate__bot__pb2.ContainsRequest.SerializeToString,
        response_deserializer=isolate__bot__pb2.ContainsReply.FromString,
        )
    self.PushBlobs = channel.stream_unary(
        '/luci.swarming.bot.FileService/PushBlobs',
        request_serializer=isolate__bot__pb2.PushBlobsRequest.SerializeToString,
        response_deserializer=isolate__bot__pb2.PushBlobsReply.FromString,
        )
    self.FetchBlobs = channel.unary_stream(
        '/luci.swarming.bot.FileService/FetchBlobs',
        request_serializer=isolate__bot__pb2.FetchBlobsRequest.SerializeToString,
        response_deserializer=isolate__bot__pb2.FetchBlobsReply.FromString,
        )


class FileServiceServicer(object):
  """FileService exposes the main operations of an Isolate server
  to upload and download blobs.
  """

  def Contains(self, request, context):
    """Unlike in the native Isolate API, it is not *necessary* to
    call Contains prior to pushing a blob, as Contains does not
    return "upload tickets." The BlobStatus returned by Contains
    will have succeeded = True if all digests were found, and
    false for any other reason (missing blobs, network error,
    etc.)
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def PushBlobs(self, request_iterator, context):
    """PushBlobs can push one or more blobs at a time (serially),
    with each blob transmitted as one or more chunks. At the
    beginning of a new blob, the chunk offset should be zero
    and the digest must be provided. The function returns true
    only if all blobs are successfully received, and returns
    as soon as an error occurs.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def FetchBlobs(self, request, context):
    """FetchBlobs takes a list of digests and returns them all as
    a stream of BlobChunks.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_FileServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Contains': grpc.unary_unary_rpc_method_handler(
          servicer.Contains,
          request_deserializer=isolate__bot__pb2.ContainsRequest.FromString,
          response_serializer=isolate__bot__pb2.ContainsReply.SerializeToString,
      ),
      'PushBlobs': grpc.stream_unary_rpc_method_handler(
          servicer.PushBlobs,
          request_deserializer=isolate__bot__pb2.PushBlobsRequest.FromString,
          response_serializer=isolate__bot__pb2.PushBlobsReply.SerializeToString,
      ),
      'FetchBlobs': grpc.unary_stream_rpc_method_handler(
          servicer.FetchBlobs,
          request_deserializer=isolate__bot__pb2.FetchBlobsRequest.FromString,
          response_serializer=isolate__bot__pb2.FetchBlobsReply.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'luci.swarming.bot.FileService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
