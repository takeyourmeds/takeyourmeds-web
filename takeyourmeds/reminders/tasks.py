from __future__ import absolute_import

from celery import shared_task
from celery.utils.log import get_task_logger

from django.contrib.staticfiles.storage import staticfiles_storage

from takeyourmeds.telephony.utils import send_sms, make_call

from .models import Reminder

logger = get_task_logger(__name__)

@shared_task()
def send_reminder_task(reminder_id):
    reminder = Reminder.objects.get(pk=reminder_id)

    if reminder.message:
        send_sms(reminder.telnumber, reminder.message)
    elif reminder.audio_url:
        make_call(
            reminder.telnumber,
            staticfiles_storage.url(reminder.audio_url),
        )
    else:
        logger.warn("Reminder %s has neither message nor url", reminder.pk)
