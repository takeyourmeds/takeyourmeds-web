import datetime
import urlparse

from django.db import models
from django.conf import settings
from django.utils.crypto import get_random_string

from .enums import TypeEnum,SourceEnum

class Reminder(models.Model):
    user = models.ForeignKey('account.User', related_name='reminders')

    type = models.IntegerField(choices=[(x.name, x.value) for x in TypeEnum])

    message = models.CharField(max_length=100, blank=True)
    audio_url = models.CharField(max_length=100, blank=True)

    phone_number = models.CharField(max_length=200)

    created = models.DateTimeField(default=datetime.datetime.utcnow)

    class Meta:
        ordering = ('created',)

    def __unicode__(self):
        return u"pk=%d type=%s phone_number=%r" % (
            self.pk,
            self.get_type_enum().name,
            self.phone_number,
        )

    def get_type_enum(self):
        return {x.value: x for x in TypeEnum}[self.type]

class Time(models.Model):
    """
    A time-of-day that this reminder should run.
    """

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
        return u"pk=%s reminder_id=%d time=%r" % (
            self.pk,
            self.reminder_id,
            self.time,
        )

class Instance(models.Model):
    """
    A specific instance of a reminder, created either when a reminder time is
    reached or a manual trigger.

    The "parent" foreign key is a ``Reminder`` and not a ``Time`` to a) allow
    for manual triggers which have no Time, and b) to allow for Time instances
        to be removed rather than marked as "disabled" which is complicated in
        the presence of ``unique_together``.
    """

    reminder = models.ForeignKey(Reminder, related_name='instances')

    source = models.IntegerField(
        choices=[(x.name, x.value) for x in SourceEnum],
    )

    created = models.DateTimeField(default=datetime.datetime.utcnow)

    class Meta:
        ordering = ('-created',)
        get_latest_by = 'created'

    def __unicode__(self):
        return u"pk=%d reminder_id=%d source=%s" % (
            self.pk,
            self.reminder_id,
            self.get_state_enum().name,
        )

    def __unicode__(self):
        return u"pk=%d reminder_id=%d: source=%s" % (
            self.pk,
            self.reminder_id,
            self.get_source_enum().name,
        )

    def get_source_enum(self):
        return {x.value: x for x in SourceEnum}[self.source]

class AbstractNotification(models.Model):
    """
    Base class for all notification types.
    """

    instance = models.ForeignKey(Instance, related_name='%(class)ss')

    ident = models.CharField(
        unique=True,
        default=lambda: get_random_string(40),
        max_length=40,
    )

    twilio_sid = models.CharField(max_length=34, unique=True)

    traceback = models.TextField()

    created = models.DateTimeField(default=datetime.datetime.utcnow)

    class Meta:
        abstract = True
        ordering = ('-created',)
        get_latest_by = 'created'

    def __unicode__(self):
        return u"pk=%d instance_id=%d twilio_sid=%r" % (
            self.pk,
            self.instance_id,
            self.twilio_sid,
        )

    @models.permalink
    def get_absolute_url(self):
        return 'reminders:%ss:status-callback' % self._meta.model_name, \
            (self.ident,)

    def get_status_callback_url(self):
        return urlparse.urljoin(settings.SITE_URL, self.get_absolute_url())
