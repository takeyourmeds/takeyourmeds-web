from __future__ import absolute_import

import traceback

from celery import shared_task

from django.conf import settings

from takeyourmeds.utils.dt import local_time
from takeyourmeds.utils.twilio import get_twilio_client

from .enums import TypeEnum, SourceEnum
from .models import Reminder, Time

@shared_task()
def schedule_reminders():
    for x in Time.objects.filter(time='%02d:00' % local_time().hour):
        trigger_reminder.delay(x.reminder_id, SourceEnum.cron.value)

@shared_task()
def trigger_reminder(reminder_id, source=SourceEnum.manual.value):
    reminder = Reminder.objects.get(pk=reminder_id)

    instance = reminder.instances.create(source=source)

    notification = getattr(
        instance,
        '%ss' % reminder.get_type_enum().name,
    ).create()

    try:
        resource = notify(notification)
    except:
        notification.traceback = traceback.format_exc()
        raise
    else:
        notification.twilio_sid = resource.sid
    finally:
        notification.save()

    return repr((reminder, instance, notification))

def notify(notification):
    reminder = notification.instance.reminder

    if reminder.type == TypeEnum.message:
        return get_twilio_client().messages.create(
            to=reminder.phone_number,
            body=reminder.message,
            from_=settings.TWILIO_FROM,
            status_callback=notification.get_status_callback_url(),
        )

    if reminder.type == TypeEnum.call:
        return get_twilio_client().calls.create(
            to=reminder.phone_number,
            from_=settings.TWILIO_FROM,
            url=notification.get_twiml_callback_url(),
            status_callback=notification.get_status_callback_url(),
        )

    raise NotImplementedError("Unhandled reminder type")
