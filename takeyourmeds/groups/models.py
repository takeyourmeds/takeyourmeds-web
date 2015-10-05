import datetime

from django.db import models
from django.utils.crypto import get_random_string

class Group(models.Model):
    name = models.CharField(max_length=255, unique=True)

    slug = models.CharField(
        unique=True,
        default=lambda: get_random_string(6).upper(),
        max_length=6,
    )

    created = models.DateTimeField(default=datetime.datetime.utcnow)

    class Meta:
        ordering = ('-created',)
        get_latest_by = 'created'

    def __unicode__(self):
        return u"#%d: %s (%s)" % (
            self.pk,
            self.name,
            self.slug,
        )
