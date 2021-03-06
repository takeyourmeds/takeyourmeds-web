import os
import copy
import email
import djcelery

from os.path import dirname, abspath
from celery.schedules import crontab

from django.utils.log import DEFAULT_LOGGING

from apps import *
from setup_warnings import *

djcelery.setup_loader()

BASE_DIR = '/usr/share/python/takeyourmeds'

# Fallback to relative location
if not __file__.startswith(BASE_DIR):
    BASE_DIR = dirname(dirname(dirname(dirname(abspath(__file__)))))

DEBUG = False
ALLOWED_HOSTS = ('*',)

SECRET_KEY = 'overriden-in-production'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'takeyourmeds',
        'USER': 'takeyourmeds',
        'PASSWORD': 'takeyourmeds',
        'HOST': '127.0.0.1',
        'PORT': '5432',
        'ATOMIC_REQUESTS': True,
    },
}

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'takeyourmeds.urls'
WSGI_APPLICATION = 'takeyourmeds.wsgi.application'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'takeyourmeds.utils.context_processors.settings_context',
            ],
            'builtins': [
                'switch_templatetag.templatetags.switch',
                'django.contrib.staticfiles.templatetags.staticfiles',
            ],
        },
    },
]

LOGIN_URL = '/login' # 'account:login'
LOGIN_REDIRECT_URL = '/' # 'static:landing'

USE_TZ = False
TIME_ZONE = 'UTC'
USE_I18N = False
USE_L10N = False
LANGUAGE_CODE = 'en-gb'
DATETIME_FORMAT = 'r' # RFC 2822

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'media'),)
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'

MEDIA_URL = '/storage/'
MEDIA_ROOT = 'overriden-in-production'
DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'

BROKER_URL = 'redis://localhost:6379/0'

CELERYBEAT_SCHEDULE = {
    'schedule-reminders': {
        'task': 'takeyourmeds.reminders.tasks.schedule_reminders',
        'schedule': crontab(minute=0),
        'relative': False,
    },
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

DEFAULT_FROM_EMAIL_NAME = "Take Your Meds"
DEFAULT_FROM_EMAIL_MAILTO = 'hello@takeyourmeds.co.uk'

DEFAULT_FROM_EMAIL = email.utils.formataddr((
    DEFAULT_FROM_EMAIL_NAME,
    DEFAULT_FROM_EMAIL_MAILTO,
))

SITE_URL = 'http://www.takeyourmeds.co.uk'

AUTH_USER_MODEL = 'account.User'

PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
)

AUTH_PASSWORD_VALIDATORS = (
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 6,
        }
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
)

MESSAGE_STORAGE = 'django.contrib.messages.storage.cookie.CookieStorage'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
        'KEY_PREFIX': 'takeyourmeds',
    }
}

# Always log to the console, even in production (ie. gunicorn)
LOGGING = copy.deepcopy(DEFAULT_LOGGING)
LOGGING['handlers']['console']['filters'] = []

SESSION_COOKIE_AGE = 86400 * 365 * 10
SESSION_COOKIE_HTTPONLY = True

STRIPE_ENABLED = True
STRIPE_SECRET_KEY = 'overriden-in-production'
STRIPE_PUBLISHABLE_KEY = 'overriden-in-production'

TWILIO_ENABLED = True
TWILIO_AUTH_TOKEN = 'overriden-in-production'
TWILIO_ACCOUNT_SID = 'overriden-in-production'

TWILIO_CALL_FROM = '+441233800896'
TWILIO_MESSAGE_FROM = 'TakeYourMed' # 11-character limit
