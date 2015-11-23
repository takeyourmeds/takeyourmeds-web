from __future__ import absolute_import

import re

from twilio.rest import TwilioRestClient

from django import forms
from django.conf import settings
from django.utils.crypto import get_random_string

re_phone_number = re.compile(r'^\d{9,14}$')

def get_twilio_client():
    if not settings.TWILIO_ENABLED:
        class Attribute(object):
            def create(self, *args, **kwargs):
                resource = Resource()
                resource.sid = get_random_string(34)
                return resource

        class Resource(object):
            pass

        class MockTwilioRestClient(object):
            calls = Attribute()
            messages = Attribute()

        return MockTwilioRestClient()

    return TwilioRestClient(
        settings.TWILIO_ACCOUNT_SID,
        settings.TWILIO_AUTH_TOKEN,
    )

def validate_phone_number(val):
    val = ''.join(val.split())

    if re_phone_number.match(val) is None:
        raise forms.ValidationError(
            "This does not appear to be a valid UK phone number.",
        )

    return val

def sanitise_phone_number(val):
    """
    We store (almost) whatever number the user provided but massage it later.
    """

    return '+44%s' % val[1:] if val.startswith('0') else val
