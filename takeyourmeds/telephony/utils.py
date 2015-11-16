from twilio.rest import TwilioRestClient

from django.conf import settings
from django.utils.crypto import get_random_string

from .models import TwilioMLCallback

def send_sms(to_number, message_text):
    """
    Send SMS message.
    """

    message = get_client().messages.create(
        to=to_number,
        body=message_text,
        from_=settings.TWILIO_FROM,
    )

    return message.sid

def make_call(to_number, audio_url):
    """
    Make a call to the specified number and play the MP3 specified in
    `audio_url`.
    """

    callback = TwilioMLCallback.objects.create(content="""
        <?xml version="1.0" encoding="UTF-8"?>
        <Response>
            <Play loop="1">{}</Play>
        </Response>
    """.format(audio_url).strip())

    call = get_client().calls.create(
        to=to_number,
        from_=settings.TWILIO_FROM,

        url=callback.get_callback_url(),
        method='GET',
    )

    return call.sid

def get_client():
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
