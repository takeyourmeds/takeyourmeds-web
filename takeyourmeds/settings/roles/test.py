from local import *

DATABASES = {'default': {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': ':memory:',
    'ATOMIC_REQUESTS': True,
}}

PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.CryptPasswordHasher',
)
AUTH_PASSWORD_VALIDATORS = ()

MEDIA_ROOT = '/tmp'
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'
