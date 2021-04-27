PY = poetry run python
PY_DIR = python
JAVA_DIR = java
PROTOS = $(wildcard proto/recap_schema/*/v*/*.proto)

.PHONY: python all java

all: python java

java:
	cd ${JAVA_DIR} && gradle build

python:
	rm -rf ${PY_DIR}/src
	mkdir ${PY_DIR}/src
	cd python && ${PY} -m grpc_tools.protoc -I../proto --python_out=src --mypy_out=src --grpc_python_out=src --mypy_grpc_out=src $(addprefix ../, ${PROTOS})
	find ${PY_DIR}/src -type d -exec touch {}/__init__.py \;
