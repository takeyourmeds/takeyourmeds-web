from datetime import datetime

import pytz
from croniter import croniter
from django.db import models

class ReminderTime(models.Model):
    reminder = models.ForeignKey('Reminder', related_name='reminder_times')
    cronstring = models.CharField(blank=True, max_length=100)
    last_run = models.DateTimeField(auto_now_add=True)

    def should_run(self):
        times = croniter(self.cronstring, self.last_run)
        return times.get_next(datetime) < datetime.now(pytz.utc)

    def run(self):
        self.reminder.dispatch_task()
        self.last_run = datetime.now(pytz.utc)
        self.save()


class Reminder(models.Model):
    message = models.CharField(blank=True, max_length=100)
    audiourl = models.CharField(blank=True, max_length=100)
    telnumber = models.CharField(max_length=200)

    def dispatch_task(self):
        from .tasks import send_reminder_task
        send_reminder_task.delay(self.pk)
