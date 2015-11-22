import datetime
import functools

from django.db import models
from django.utils.crypto import get_random_string

from .managers import RecordRequestManager

class RecordRequest(models.Model):
    """
    Manages a request to create a custom audio message.
    """

    user = models.ForeignKey(
        'account.User',
        related_name='audio_recording_requests',
    )

    phone_number = models.CharField(max_length=200)

    ident = models.CharField(
        unique=True,
        default=functools.partial(get_random_string, 40),
        max_length=40,
    )

    # Nullable as we need to create the instance before saving
    twilio_sid = models.CharField(
        max_length=34,
        null=True,
        unique=True,
        default=None,
    )

    created = models.DateTimeField(default=datetime.datetime.utcnow)

    objects = RecordRequestManager()

    class Meta:
        ordering = ('-created',)
        get_latest_by = 'created'

    def __unicode__(self):
        return u"pk=%d user_id=%d twilio_sid=%r phone_number=%r" % (
            self.pk,
            self.user_id,
            self.twilio_sid,
            self.phone_number,
        )
