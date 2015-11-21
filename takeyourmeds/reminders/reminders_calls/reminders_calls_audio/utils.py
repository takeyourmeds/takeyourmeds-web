from django.conf import settings

from takeyourmeds.utils.url import resolve_absolute
from takeyourmeds.utils.twilio import get_twilio_client

def create(user):
    recording-

    return get_twilio_client().calls.create(
        to=reminder.get_phone_number(),
        from_=settings.TWILIO_CALL_FROM,
        url=resolve_absolute(
            'reminders:calls:twiml-callback', call.ident,
        ),
        if_machine='Hangup',
        status_callback=resolve_absolute(
            'reminders:calls:status-callback', call.ident,
        ),
    )

