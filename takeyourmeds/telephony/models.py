import datetime
import urlparse

from django.db import models
from django.conf import settings
from django.utils.crypto import get_random_string

class TwilioMLCallback(models.Model):
    """
    Persists a Twilio ML snippet so callbacks can retrieve it later.

    Might be nicer to work out what to do when the call/etc. comes in to avoid
    configuration race conditions, but this is better than the /tmp solution.
    """

    ident = models.CharField(
        unique=True,
        default=lambda: get_random_string(40),
        max_length=40,
    )

    content = models.TextField()

    created = models.DateTimeField(default=datetime.datetime.utcnow)

    class Meta:
        ordering = ('-created',)
        get_latest_by = 'created'

    def __unicode__(self):
        return u"#%d: %s" % (self.pk, self.ident)

    @models.permalink
    def get_absolute_url(self):
        return 'telephony:callback', (self.ident,)

    def get_callback_url(self):
        return urlparse.urljoin(settings.SITE_URL, self.get_absolute_url())
