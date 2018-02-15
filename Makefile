.PHONY: install install-requirements virtualenv clean

VIRTUALENV=virtualenv
VIRTUALENV_DIR=${PWD}/env
PIP=${VIRTUALENV_DIR}/bin/pip
PIP_INSTALL=${PIP} install
PYTHON=${VIRTUALENV_DIR}/bin/python

default: install

install: install-requirements
	${PYTHON} setup.py develop

install-requirements: virtualenv
	${PIP_INSTALL} -r requirements.txt

virtualenv:
	if [ ! -e ${PIP} ]; then \
	${VIRTUALENV} -p python3 ${VIRTUALENV_DIR}; \
	fi
	${PIP_INSTALL} --upgrade pip

clean:
	find . -name '*.pyc' -exec rm -fv {} \;
	find . -name '*.pyo' -exec rm -fv {} \;
	find . -depth -name '__pycache__' -exec rm -rfv {} \;
	-rm -rfv ${VIRTUALENV_DIR} && \
	find . -depth -name '*.egg-info' -exec rm -rfv {} \;