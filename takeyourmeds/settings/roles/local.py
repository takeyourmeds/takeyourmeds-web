DEBUG = True

TWILIO_CONFIG = {
    'ACCOUNT_SID': 'XXX',
    'AUTH_TOKEN': 'XXX',
    'FROM_NUMBER': '0000',
    'ROOT_URL': 'http://127.0.0.1:8000/telephony/info',
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
