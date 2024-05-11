#!/bin/bash 
# ref : https://zhuanlan.zhihu.com/p/338725233

python3 -m grpc_tools.protoc -I=. --python_out=. --grpc_python_out=. ./pb/server.proto

