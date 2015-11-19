from django.conf import settings

from takeyourmeds.utils.url import resolve_absolute
from takeyourmeds.utils.twilio import get_twilio_client

def trigger(call):
    reminder = call.instance.reminder

    return get_twilio_client().calls.create(
        to=reminder.get_phone_number(),
        from_=settings.TWILIO_CALL_FROM,
        url=call.get_twiml_callback_url(),
        status_callback=resolve_absolute(
            'reminders:calls:status-callback', call.ident,
        ),
    )
