DEBUG = True

SITE_URL = 'http://127.0.0.1:8000'

TWILIO_CONFIG = {
    'ACCOUNT_SID': 'XXX',
    'AUTH_TOKEN': 'XXX',
    'FROM_NUMBER': '0000',
    'ROOT_URL': '%s/telephony/info' % SITE_URL,
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
