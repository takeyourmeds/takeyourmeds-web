from __future__ import absolute_import

from celery import shared_task
from celery.utils.log import get_task_logger

from django.contrib.staticfiles.storage import staticfiles_storage

from takeyourmeds.utils.dt import local_time
from takeyourmeds.telephony.utils import send_sms, make_call

from .models import Reminder, Time

logger = get_task_logger(__name__)

@shared_task()
def schedule_reminders():
    for x in Time.objects.filter(time='%02d:00' % local_time().hour):
        x.reminder.trigger()

@shared_task()
def trigger_reminder(reminder_id):
    reminder = Reminder.objects.get(pk=reminder_id)

    if reminder.message:
        send_sms(reminder.phone_number, reminder.message)
        return

    if reminder.audio_url:
        make_call(
            reminder.phone_number,
            staticfiles_storage.url(reminder.audio_url),
        )
        return

    logger.error("Unhandled reminder %d", reminder.pk)
