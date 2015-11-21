import datetime
import functools

from django.db import models

class RecordRequest(models.Model):
    """
    Manages a request to create a custom audio message.
    """

    user = models.ForeignKey(
        'auth.User',
        related_name='audio_recording_request',
    )

    ident = models.CharField(
        unique=True,
        default=functools.partial(get_random_string, 40),
        max_length=40,
    )

    created = models.DateTimeField(default=datetime.datetime.utcnow)

    class Meta:
        ordering = ('-created',)
        get_latest_by = 'created'

    def __unicode__(self):
        return u"#%d: %s" % (
            self.pk,
            self.title,
        )
