#!/usr/bin/env python
import os
import sys
from cherrypy import wsgiserver

from kskgcomplain.wsgi import application

#ip = os.environ['OPENSHIFT_PYTHON_IP']
#port = int(os.environ['OPENSHIFT_PYTHON_PORT'])
#host_name = os.environ['OPENSHIFT_GEAR_DNS']


#server = wsgiserver.CherryPyWSGIServer((ip, port), application, server_name=host_name)
#server.start()
