from django.conf import settings
from django.contrib import auth

def login(request, user):
    user.backend = settings.AUTHENTICATION_BACKENDS[0]
    auth.login(request, user)
