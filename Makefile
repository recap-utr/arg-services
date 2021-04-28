VERSION = 0.1.3
PY = poetry run python
PY_DIR = python
JAVA_DIR = java
PROTOS = $(wildcard proto/arg_services/*/v*/*.proto)

.PHONY: python all java version

all: python java

version:
	cd python && poetry version ${VERSION}

java:
	cd ${JAVA_DIR} && gradle build

publish-python:
	cd python && poetry publish --build

python:
	rm -rf ${PY_DIR}/src
	mkdir ${PY_DIR}/src
	cd python && ${PY} -m grpc_tools.protoc -I../proto --python_out=src --mypy_out=src --grpc_python_out=src --mypy_grpc_out=src $(addprefix ../, ${PROTOS})
	find ${PY_DIR}/src/arg_services -type d -exec touch {}/__init__.py \;
