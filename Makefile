VERSION = 0.3.9
TARGET = gen
SOURCE = src
PY = python
JAVA = java
TS = typescript
PROJECT = arg_services
# PROTOS = $(wildcard proto/${PROJECT}/*/v*/*.proto)

.PHONY: generate
generate: version
	rm -rf ${TARGET}
	buf generate

	# All
	find ${TARGET}/${PY} ${TARGET}/${TS} ${TARGET}/${JAVA} -type d -maxdepth 0 -exec cp README.md {} \;

	# Python
	find ${TARGET}/${PY}/${PROJECT} -type d -exec touch {}/__init__.py \;
	cp -f ${SOURCE}/${PY}/${PROJECT}/__init__.py ${TARGET}/${PY}/${PROJECT}
	cp -r ${SOURCE}/${PY}/{poetry.lock,pyproject.toml} ${TARGET}/${PY}

	# Typescript
	cp ${SOURCE}/${TS}/{package-lock.json,package.json} gen/${TS}

.PHONY: version
version:
	cd ${SOURCE}/${PY} && poetry version ${VERSION}
	cd ${SOURCE}/${TS} && npm version --allow-same-version true --git-tage-version false ${VERSION}

.PHONY: publish
publish: generate
	# Python
	cd ${TARGET}/${PY} && poetry publish --build

	# Typescript
	cd ${TARGET}/${TS} && npm publish --access public

	# Buf Registry
	buf push
