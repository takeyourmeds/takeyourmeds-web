from __future__ import absolute_import

import traceback

from celery import shared_task

from django.conf import settings

from takeyourmeds.utils.dt import local_time
from takeyourmeds.utils.twilio import get_twilio_client

from .enums import TypeEnum, SourceEnum
from .models import Reminder, Instance, Time

@shared_task()
def schedule_reminders():
    for x in Time.objects.filter(time='%02d:00' % local_time().hour):
        trigger_reminder.delay(x.reminder_id, SourceEnum.cron.value)

@shared_task()
def trigger_reminder(reminder_id, source=SourceEnum.manual.value):
    reminder = Reminder.objects.get(pk=reminder_id)

    instance = reminder.instances.create(source=source)

    return repr(create_notification(instance))

@shared_task()
def trigger_instance(instance_id):
    instance = Instance.objects.get(pk=instance_id)

    return repr(create_notification(instance))

def create_notification(instance):
    """
    Create and fire an appropriate notification for this instance.
    """

    notification = getattr(
        instance,
        '%ss' % instance.reminder.get_type_enum().name,
    ).create()

    # We won't get a callback from Twilio if Twilio is disabled, so let's set a
    # special state to not have confusing "in progress" messages outside of a
    # live environment.
    if not settings.TWILIO_ENABLED:
        notification.state = 10 # twilio_disabled

    try:
        resource = notify(notification)
    except:
        notification.state = 20 # failed
        notification.traceback = traceback.format_exc()
        raise
    else:
        notification.twilio_sid = resource.sid
    finally:
        notification.save()

    return notification

def notify(notification):
    """
    Actually perform the notification.
    """

    reminder = notification.instance.reminder

    if reminder.type == TypeEnum.message:
        return get_twilio_client().messages.create(
            to=reminder.get_phone_number(),
            body=reminder.message,
            from_=settings.TWILIO_MESSAGE_FROM,
            status_callback=notification.get_status_callback_url(),
        )

    if reminder.type == TypeEnum.call:
        return get_twilio_client().calls.create(
            to=reminder.get_phone_number(),
            from_=settings.TWILIO_CALL_FROM,
            url=notification.get_twiml_callback_url(),
            status_callback=notification.get_status_callback_url(),
        )

    raise NotImplementedError("Unhandled reminder type")
