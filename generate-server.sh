#!/bin/sh

pip3 install --no-cache-dir -r requirements.txt

MODULE=simple_registration_server

python3 -m swagger_py_codegen -s src/main/resources/api.yaml --ui --spec $MODULE -p server_api

pip3 install --no-cache-dir -r ${MODULE}/requirements.txt
