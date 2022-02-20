VERSION = 0.2.2
DOC_DIR = doc
PY = poetry run python
PY_DIR = python
JAVA_DIR = java
TS_DIR = typescript
PROJECT = arg_services
PROTOS = $(wildcard proto/${PROJECT}/*/v*/*.proto)

.PHONY: all
all: python java typescript doc

.PHONY: publish doc
publish: version publish-python

.PHONY: version
version: doc
	cd python && poetry version ${VERSION}

.PHONY: java
java: doc
	cd ${JAVA_DIR} && mvn package

.PHONY: typescript
typescript: doc
	cd ${TS_DIR} && protoc -I=../proto ${PROTOS:proto/%=%} \
                      --js_out=import_style=commonjs:. \
                      --grpc-web_out=import_style=typescript,mode=grpcwebtext:.

.PHONY: publish-python
publish-python: python
	cd ${PY_DIR} && poetry publish --build

.PHONY: python
python: doc
	rm -rf ${PY_DIR}/${PROJECT}
	mkdir ${PY_DIR}/${PROJECT}
	cd python && ${PY} -m grpc_tools.protoc -I../proto --python_out=. --mypy_out=. --grpc_python_out=. --mypy_grpc_out=. $(addprefix ../, ${PROTOS})
	find ${PY_DIR}/${PROJECT} -type d -exec touch {}/__init__.py \;

.PHONY: doc
doc:
	protoc -I proto ${PROTOS:proto/%=%} --doc_out=${DOC_DIR} --doc_opt=markdown,README.md
