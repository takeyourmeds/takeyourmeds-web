import datetime

from django.db import models

from .enums import StateEnum

class Entry(models.Model):
    reminder = models.ForeignKey(
        'reminders.Reminder',
        related_name='log_entries',
    )

    state = models.IntegerField(
        choices=[(x.name, x.value) for x in StateEnum],
    )

    traceback = models.TextField()

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
