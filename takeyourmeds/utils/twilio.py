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

def sanitise_phone_number(val):
    """
    We store (almost) whatever number the user provided but massage it later.
    """

    return '+44%s' % val[1:] if val.startswith('0') else val
