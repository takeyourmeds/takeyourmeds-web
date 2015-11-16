from __future__ import absolute_import

import urlparse
import traceback

from celery import shared_task

from django.conf import settings
from django.contrib.staticfiles.storage import staticfiles_storage

from takeyourmeds.utils.dt import local_time
from takeyourmeds.telephony.utils import send_sms, make_call

from .enums import SourceEnum
from .models import Reminder, Time

@shared_task()
def schedule_reminders():
    for x in Time.objects.filter(time='%02d:00' % local_time().hour):
        trigger_reminder.delay(x.reminder_id, SourceEnum.cron.value)

@shared_task()
def trigger_reminder(reminder_id, source=SourceEnum.manual.value):
    reminder = Reminder.objects.get(pk=reminder_id)
    instance = reminder.instances.create(source=source)

    notification = _create_notification(reminder, instance)

    try:
        notification.twilio_sid = _trigger_reminder(reminder)
    except:
        notification.traceback = traceback.format_exc()
        raise
    finally:
        notification.save()

    return repr((reminder, instance, notification))

def _create_notification(reminder, instance):
    if reminder.message:
        return instance.messages.create()

    if reminder.audio_url:
        return instance.calls.create()

    raise NotImplementedError("Unhandled reminder type")

def _trigger_reminder(reminder):
    if reminder.message:
        return send_sms(reminder.phone_number, reminder.message)

    if reminder.audio_url:
        # Ensure we have an absolute URL
        absolute_audio_url = urlparse.urljoin(
            settings.SITE_URL,
            staticfiles_storage.url(reminder.audio_url),
        )

        return make_call(reminder.phone_number, absolute_audio_url)

    raise NotImplementedError("Unhandled reminder type")
