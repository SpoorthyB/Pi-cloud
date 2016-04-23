import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME':  'microblog',
        'USER': 'vagrant',
	'PASSWORD':'',
	'HOST':'',
	'PORT':'',
    }
}

