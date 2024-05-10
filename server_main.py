

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

    def DownLoadFile(self, request, context):

        file_name = request.file_name
        logging.debug("client request download file: %s, device id : %d" % (file_name, request.device_id))

        try:
            with open(os.path.join(default_file_path, file_name), 'rb') as f :
                file_content = f.read()
            response = server_pb2.DownloadFileResponse(content = file_content)
            return response 

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


    try :
        while True:
            time.sleep(1000)
    except KeyboardInterrupt:
        server.stop(0)