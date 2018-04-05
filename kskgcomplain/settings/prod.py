from .base import *
DEBUG = False
SECRET_KEY = os.environ.get('COMPLAIN_SECRET_KEY')
DB_USERNAME = os.environ.get('COMPLAIN_DB_USERNAME')
DB_PASSWORD = os.environ.get('COMPLAIN_DB_PASSWORD')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(DATA_DIR, 'db.sqlite3'),
    }
}

ALLOWED_HOSTS = ['*']
