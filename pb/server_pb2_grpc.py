# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from pb import server_pb2 as pb_dot_server__pb2

GRPC_GENERATED_VERSION = '1.63.0'
GRPC_VERSION = grpc.__version__
EXPECTED_ERROR_RELEASE = '1.65.0'
SCHEDULED_RELEASE_DATE = 'June 25, 2024'
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    warnings.warn(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in pb/server_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class FileServerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetVersionList = channel.unary_unary(
                '/ota.FileServer/GetVersionList',
                request_serializer=pb_dot_server__pb2.GetVersionRequest.SerializeToString,
                response_deserializer=pb_dot_server__pb2.GetVersionResponse.FromString,
                _registered_method=True)
        self.DownLoadFile = channel.unary_stream(
                '/ota.FileServer/DownLoadFile',
                request_serializer=pb_dot_server__pb2.DownloadFileRequest.SerializeToString,
                response_deserializer=pb_dot_server__pb2.DownloadFileResponse.FromString,
                _registered_method=True)


class FileServerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetVersionList(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DownLoadFile(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_FileServerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetVersionList': grpc.unary_unary_rpc_method_handler(
                    servicer.GetVersionList,
                    request_deserializer=pb_dot_server__pb2.GetVersionRequest.FromString,
                    response_serializer=pb_dot_server__pb2.GetVersionResponse.SerializeToString,
            ),
            'DownLoadFile': grpc.unary_stream_rpc_method_handler(
                    servicer.DownLoadFile,
                    request_deserializer=pb_dot_server__pb2.DownloadFileRequest.FromString,
                    response_serializer=pb_dot_server__pb2.DownloadFileResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ota.FileServer', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class FileServer(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetVersionList(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/ota.FileServer/GetVersionList',
            pb_dot_server__pb2.GetVersionRequest.SerializeToString,
            pb_dot_server__pb2.GetVersionResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def DownLoadFile(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(
            request,
            target,
            '/ota.FileServer/DownLoadFile',
            pb_dot_server__pb2.DownloadFileRequest.SerializeToString,
            pb_dot_server__pb2.DownloadFileResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
