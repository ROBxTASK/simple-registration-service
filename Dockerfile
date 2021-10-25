FROM python:3.8-slim-buster

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY . /usr/src/app/

RUN ./generate-server.sh

#COPY simple_registration_server /usr/src/app

#RUN swagger_py_codegen -s src/main/resources/api.yaml --ui --spec simple_registration_server -p server_api

#RUN pip3 install --no-cache-dir -r simple_registration_server/requirements.txt

#RUN touch simple_registration_server/server_api/__main__.py

EXPOSE 5000

WORKDIR /usr/src/app/simple_registration_server/server_api

ENTRYPOINT ["python"]
CMD ["__init__.py"]

#CMD ["-m", "simple_registration_server.server_api"]
