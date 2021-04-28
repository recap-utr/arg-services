VERSION = 0.1.4
PY = poetry run python
PY_DIR = python
JAVA_DIR = java
PROJECT = arg_services
PROTOS = $(wildcard proto/${PROJECT}/*/v*/*.proto)

.PHONY: python all java version

all: python java

version:
	cd python && poetry version ${VERSION}

java:
	cd ${JAVA_DIR} && gradle build

publish-python:
	cd python && poetry publish --build

python:
	rm -rf ${PY_DIR}/${PROJECT}
	mkdir ${PY_DIR}/${PROJECT}
	cd python && ${PY} -m grpc_tools.protoc -I../proto --python_out=. --mypy_out=. --grpc_python_out=. --mypy_grpc_out=. $(addprefix ../, ${PROTOS})
	find ${PY_DIR}/${PROJECT} -type d -exec touch {}/__init__.py \;
