from django.conf import settings

from takeyourmeds.utils.url import resolve_absolute
from takeyourmeds.utils.twilio import get_twilio_client, sanitise_phone_number

def trigger(message):
    reminder = message.instance.reminder

    return get_twilio_client().messages.create(
        to=sanitise_phone_number(reminder.phone_number),
        body=reminder.message,
        from_=settings.TWILIO_MESSAGE_FROM,
        status_callback=resolve_absolute(
            'reminders:messages:status-callback', message.ident,
        ),
    )
