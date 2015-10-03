from django import forms
from django.conf import settings
from django.contrib import auth

def login(request, user):
    user.backend = settings.AUTHENTICATION_BACKENDS[0]
    auth.login(request, user)

def validate_password(val):
    min_length = 6

    if not val:
        return val

    if len(val) < min_length:
        raise forms.ValidationError(
            "Password must be at least %d characters" % min_length
        )

    return val
