from __future__ import absolute_import

from celery import shared_task
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)

from .models import Reminder

@shared_task()
def send_reminder_task(reminder_id):
    reminder = Reminder.objects.get(pk=reminder_id)
    logger.debug('reminder sending: %s', reminder.pk)
    # reminder.do_what_ross_says()
