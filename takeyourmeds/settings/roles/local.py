import os

from django.utils.log import DEFAULT_LOGGING as LOGGING

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

DEBUG = True

SITE_URL = 'http://127.0.0.1:8000'
MEDIA_ROOT = os.path.join(BASE_DIR, 'storage')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite'),
        'ATOMIC_REQUESTS': True,
    },
}

TWILIO_ENABLED = False

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}

BROKER_URL = 'memory://'
CELERY_ALWAYS_EAGER = True
CELERY_EAGER_PROPAGATES_EXCEPTIONS = True

STRIPE_ENABLED = False
