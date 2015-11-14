import datetime

from django.db import models

from .enums import StateEnum

class Instance(models.Model):
    reminder = models.ForeignKey(
        'reminders.Reminder',
        related_name='instances',
    )

    state = models.IntegerField(
        choices=[(x.name, x.value) for x in StateEnum],
    )

    traceback = models.TextField()
    twilio_sid = models.CharField(max_length=34)

    created = models.DateTimeField(default=datetime.datetime.utcnow)

    class Meta:
        ordering = ('-created',)
        get_latest_by = 'created'

    def __unicode__(self):
        return u"#%d: %s (%s)" % (
            self.pk,
            self.reminder_id,
            self.created,
        )
