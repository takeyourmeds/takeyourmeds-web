import datetime

from django.db import models

from croniter import croniter

class Reminder(models.Model):
    user = models.ForeignKey('account.User', related_name='reminders')
    message = models.CharField(blank=True, max_length=100)
    audiourl = models.CharField(blank=True, max_length=100)
    telnumber = models.CharField(max_length=200)

    def dispatch_task(self):
        from .tasks import send_reminder_task
        send_reminder_task.delay(self.pk)

class Time(models.Model):
    reminder = models.ForeignKey('Reminder', related_name='times')
    cronstring = models.CharField(blank=True, max_length=100)
    last_run = models.DateTimeField(default=datetime.datetime.utcnow)

    def should_run(self):
        times = croniter(self.cronstring, self.last_run)

        return times.get_next(datetime.datetime) < \
            datetime.datetime.utcnow()

    def run(self):
        self.reminder.dispatch_task()
        self.last_run = datetime.datetime.utcnow()
        self.save()
