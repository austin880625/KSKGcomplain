#!/bin/bash
~/python/virtenv/venv/bin/activate
gunicorn kskgcomplain.wsgi 127.0.0.1:8071
