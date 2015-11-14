from __future__ import absolute_import

import traceback

from celery import shared_task
from celery.utils.log import get_task_logger

from django.contrib.staticfiles.storage import staticfiles_storage

from takeyourmeds.utils.dt import local_time
from takeyourmeds.telephony.utils import send_sms, make_call

from .models import Reminder, Time
from .reminders_logging.enums import StateEnum

logger = get_task_logger(__name__)

@shared_task()
def schedule_reminders():
    for x in Time.objects.filter(time='%02d:00' % local_time().hour):
        trigger_reminder.delay(x.reminder_id)

@shared_task()
def trigger_reminder(reminder_id):
    reminder = Reminder.objects.get(pk=reminder_id)

    entry = reminder.log_entries.create(
        state=StateEnum.in_progress,
    )

    try:
        entry.state = StateEnum.success
        entry.twilio_sid = _trigger_reminder(reminder)
    except Exception, exc:
        entry.state = StateEnum.error
        entry.traceback = traceback.format_exc()
        raise
    finally:
        entry.save()

def _trigger_reminder(reminder):
    if reminder.message:
        return send_sms(reminder.phone_number, reminder.message)

    if reminder.audio_url:
        return make_call(
            reminder.phone_number,
            staticfiles_storage.url(reminder.audio_url),
        )

    raise NotImplementedError("Unhandled reminder action")
