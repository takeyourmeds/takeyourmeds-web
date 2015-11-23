import datetime

from django.db import models

class Recording(models.Model):
    user = models.ForeignKey(
        'account.User',
        related_name='recordings',
    )

    audio_file = models.FileField()

    created = models.DateTimeField(default=datetime.datetime.utcnow)

    class Meta:
        ordering = ('-created',)
        get_latest_by = 'created'

    def __unicode__(self):
        return u"pk=%d title=%r" % (
            self.pk,
            self.title,
        )
