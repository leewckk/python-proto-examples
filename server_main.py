

import logging 
import os   
import grpc 
import time

from concurrent import futures 
from pb import server_pb2 , server_pb2_grpc


LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(level=logging.DEBUG, format=LOG_FORMAT)

default_file_path = "./"

class FileServer(server_pb2_grpc.FileServerServicer) :

    def GetVersionList(self, request, context):
        # 在这里实现获取版本列表的逻辑
        version_info1 = server_pb2.VersionInfo(device_type=1, version=100, file_name="file1.bin")
        version_info2 = server_pb2.VersionInfo(device_type=2, version=200, file_name="file2.bin")
        response = server_pb2.GetVersionResponse(version_infos=[version_info1, version_info2])
        return response

    def DownLoadFile(self, request, context):

        file_name = request.file_name
        logging.debug("client request download file: %s, device id : %d" % (file_name, request.device_id))

        try:
            with open(os.path.join(default_file_path, file_name), 'rb') as f :
                while True:
                    chunk = f.read(1024)
                    if not chunk:
                        break
                    logging.info("chunk is not null, size: %d" % (len(chunk)))
                    response = server_pb2.DownloadFileResponse(content = chunk)
                    yield response
                # file_content = f.read()
            # return response 

            logging.warning("file down load done !!!!")

        except Exception as e :

            logging.error(e)
            return server_pb2.DownloadFileResponse()

    

if __name__ == "__main__":

    port = '[::]:26666'

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    server_pb2_grpc.add_FileServerServicer_to_server(FileServer(),server)
    server.add_insecure_port(port)
    server.start()
    logging.warning("grpc server startup at %s" % (port))

    server.wait_for_termination()
