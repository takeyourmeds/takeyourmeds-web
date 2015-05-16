from datetime import datetime

import pytz
from croniter import croniter
from django.db import models


class Reminder(models.Model):
    cronstring = models.CharField(blank=True, max_length=100)
    message = models.CharField(blank=True, max_length=100)
    audiourl = models.CharField(blank=True, max_length=100)
    telnumber = models.CharField(max_length=200)
    last_run = models.DateTimeField(auto_now_add=True)

    def should_run(self):
        times = croniter(self.crontab, self.last_run)
        return times.get_next(datetime) < datetime.now(pytz.utc)

    def dispatch_task(self):
        from .tasks import send_reminder_task
        send_reminder_task.delay(self.pk)
        self.last_run = datetime.now(pytz.utc)
        self.save()
