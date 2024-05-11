import logging
import os
import grpc
from pb import server_pb2, server_pb2_grpc

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(level=logging.DEBUG, format=LOG_FORMAT)

default_download_path = "./download/"
default_download_file = "test.tar.gz"

if __name__ == "__main__":

    # port = '[::]:26666'

    channel = grpc.insecure_channel('localhost:26666', options=[
        ('grpc.max_receive_message_length', 2000*1024*1024)     # max size 2000MB
    ])

    stub = server_pb2_grpc.FileServerStub(channel=channel)
    request = server_pb2.DownloadFileRequest(file_name = default_download_file, device_id = 1)
    try:
        file_contents = stub.DownLoadFile(request)

        with open(os.path.join(default_download_path , default_download_file), 'wb') as f:
            for file_content in file_contents:
                f.write(file_content.content)

        logging.info("file download success , download path: %s " % (os.path.join(default_download_path, default_download_file)))

    except Exception as e:
        logging.error(e)


    request = server_pb2.GetVersionRequest(device_type = 1)
    response = stub.GetVersionList(request)
    for version_info in response.version_infos:
        logging.info("Device Type: %s, version: %s, filename: %s" % (version_info.device_type, version_info.version, version_info.file_name))