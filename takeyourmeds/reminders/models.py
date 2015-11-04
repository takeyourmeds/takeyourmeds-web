import datetime

from django.db import models

class Reminder(models.Model):
    user = models.ForeignKey('account.User', related_name='reminders')

    message = models.CharField(max_length=100, blank=True)
    audio_url = models.CharField(max_length=100)

    phone_number = models.CharField(max_length=200)

    created = models.DateTimeField(default=datetime.datetime.utcnow)

    class Meta:
        ordering = ('created',)

    def trigger(self):
        from .tasks import trigger_reminder
        trigger_reminder.delay(self.pk)

class Time(models.Model):
    reminder = models.ForeignKey('Reminder', related_name='times')

    time = models.CharField(max_length=5)
    last_run = models.DateTimeField(default=datetime.datetime.utcnow)

    created = models.DateTimeField(default=datetime.datetime.utcnow)

    class Meta:
        ordering = ('time',)
        unique_together = (
            ('reminder', 'time'),
        )

    def __unicode__(self):
        return u"#%d: %s: %s" % (
            self.pk,
            self.reminder,
            self.time,
        )

    def should_run(self):
        return True
