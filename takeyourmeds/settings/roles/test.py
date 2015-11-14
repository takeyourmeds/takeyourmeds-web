from local import *

DATABASES = {'default': {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': ':memory:',
    'ATOMIC_REQUESTS': True,
}}

PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.CryptPasswordHasher',
)

STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'
