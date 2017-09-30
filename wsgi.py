"""
WSGI config for kskgcomplain project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "kskgcomplain.settings")

application = get_wsgi_application()

#!/usr/bin/env python
#import os
#import sys
#from cherrypy import wsgiserver

#from kskgcomplain.wsgi import application

#ip = os.environ['OPENSHIFT_PYTHON_IP']
#port = int(os.environ['OPENSHIFT_PYTHON_PORT'])
#host_name = os.environ['OPENSHIFT_GEAR_DNS']


#server = wsgiserver.CherryPyWSGIServer((ip, port), application, server_name=host_name)
#server.start()
