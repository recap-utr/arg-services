VERSION = 0.1.24
PY = poetry run python
PY_DIR = python
JAVA_DIR = java
TS_DIR = typescript
PROJECT = arg_services
PROTOS = $(wildcard proto/${PROJECT}/*/v*/*.proto)

.PHONY: python all java typescript version publish-python

all: python java typescript

publish: version publish-python

version:
	cd python && poetry version ${VERSION}

java:
	cd ${JAVA_DIR} && mvn package

typescript:
	cd ${TS_DIR} && protoc -I=../proto ${PROTOS:proto/%=%} \
                      --js_out=import_style=commonjs:. \
                      --grpc-web_out=import_style=typescript,mode=grpcwebtext:.

publish-python: python
	cd ${PY_DIR} && poetry publish --build

python:
	rm -rf ${PY_DIR}/${PROJECT}
	mkdir ${PY_DIR}/${PROJECT}
	cd python && ${PY} -m grpc_tools.protoc -I../proto --python_out=. --mypy_out=. --grpc_python_out=. --mypy_grpc_out=. $(addprefix ../, ${PROTOS})
	find ${PY_DIR}/${PROJECT} -type d -exec touch {}/__init__.py \;
