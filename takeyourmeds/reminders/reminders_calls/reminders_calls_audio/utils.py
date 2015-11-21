from django.conf import settings

from takeyourmeds.utils.url import resolve_absolute
from takeyourmeds.utils.twilio import get_twilio_client, sanitise_phone_number

def create(user, phone_number):
    instance = user.audio_recording_request.create(
        phone_number=phone_number,
    )

    resource = get_twilio_client().calls.create(
        to=sanitise_phone_number(instance.phone_number),
        from_=settings.TWILIO_CALL_FROM,
        url=resolve_absolute(
            'reminders:calls:audio:twiml-callback', instance.ident,
        ),
    )

    instance.twilio_sid = resource.sid
    instance.save(update_fields=('twilio_sid',))

    return instance
