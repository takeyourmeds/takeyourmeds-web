from django.conf import settings

from takeyourmeds.utils.url import resolve_absolute
from takeyourmeds.utils.twilio import get_twilio_client

def trigger(message):
    reminder = message.instance.reminder

    return get_twilio_client().messages.create(
        to=reminder.get_phone_number(),
        body=reminder.message,
        from_=settings.TWILIO_MESSAGE_FROM,
        status_callback=resolve_absolute(message),
    )
