import os
import uuid
import urlparse

from twilio.rest import TwilioRestClient

from django.conf import settings
from django.core.urlresolvers import reverse

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

    name = str(uuid.uuid4())

    # Write out the XML with the URL of the audio
    _write_twiml(name, audio_url)

    callback_url = urlparse.urljoin(
        settings.SITE_URL,
        reverse('telephony:info', kwargs={'uuid': name})
    )

    call = get_client().calls.create(
        to=to_number,
        from_=settings.TWILIO_FROM,
        url=callback_url,
        method='GET',
        fallback_method='GET',
        status_callback_method='GET',
        record='false',
    )

    return call.sid

def get_client():
    if not settings.TWILIO_ENABLED:
        class Attribute(object):
            def create(self, *args, **kwargs):
                resource = Resource()
                resource.sid = str(uuid.uuid4())[:34]
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

def _write_twiml(name, audio_url):
    # FIXME: Not /tmp, please!

    # Generate XML file, save with name
    with open(os.path.join('/tmp/', '%s.xml' % name), 'w') as f:
        print >>f, """
            <?xml version="1.0" encoding="UTF-8"?>
            <Response>
                <Play loop="1">{}</Play>
            </Response>
        """.format(audio_url).strip()