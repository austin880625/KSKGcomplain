from .base import *
DEBUG = False
SECRET_KEY = os.environ.get('COMPLAIN_SECRET_KEY')
DB_USERNAME = os.environ.get('COMPLAIN_DB_USERNAME')
DB_PASSWORD = os.environ.get('COMPLAIN_DB_PASSWORD')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'local_complain',
        'USER': DB_USERNAME,
        'PASSWORD': DB_PASSWORD,
        'HOST': 'localhost',
        'POST': '',
    }
}

ALLOWED_HOSTS = ['*']
