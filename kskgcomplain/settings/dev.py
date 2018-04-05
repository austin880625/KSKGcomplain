from .base import *
DEBUG = True
SECRET_KEY = 'g+x1et$gxgmst6&gqtmpzndk$s!!9rmain8nm5gp2m!&74$1#^'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(DATA_DIR, 'db.sqlite3'),
    }
}

ALLOWED_HOSTS = ['*']
