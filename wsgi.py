#!/bin/bash
source ~/python/virtenv/bin/activate
gunicorn kskgcomplain.wsgi 127.0.0.1:8071
