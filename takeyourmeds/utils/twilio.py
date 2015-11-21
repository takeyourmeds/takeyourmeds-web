from __future__ import absolute_import

from twilio.rest import TwilioRestClient

from django.conf import settings
from django.utils.crypto import get_random_string

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

def sanitise_phone_number(phone_number):
    """
    We store whatever number the user provided but massage it later.
    """

    return '+44%s' % phone_number[1:] if \
        phone_number.startswith('0') else phone_number
