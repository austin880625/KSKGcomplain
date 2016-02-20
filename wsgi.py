#!/usr/bin/python
import os
import sys

virtenv=os.environ['OPENSHIFT_PYTHON_DIR']+'/virtenv/venv/bin/activate'
os.system(virtenv)
ip = os.environ['OPENSHIFT_PYTHON_IP']
port = os.environ['OPENSHIFT_PYTHON_PORT']
host_name = os.environ['OPENSHIFT_GEAR_DNS']
os.system('gunicorn kskgcomplain.wsgi localhost:'+port)
