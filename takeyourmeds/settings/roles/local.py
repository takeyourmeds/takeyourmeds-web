DEBUG = True

SITE_URL = 'http://127.0.0.1:8000'

TWILIO_ENABLED = False

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}
