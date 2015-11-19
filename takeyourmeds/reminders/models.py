import datetime
import functools

from django.db import models
from django.utils.crypto import get_random_string

from .enums import TypeEnum,SourceEnum

class Reminder(models.Model):
    user = models.ForeignKey('account.User', related_name='reminders')

    type = models.IntegerField(choices=[(x.name, x.value) for x in TypeEnum])

    message = models.CharField(max_length=100, blank=True)
    audio_url = models.CharField(max_length=100, blank=True)

    phone_number = models.CharField(max_length=200)

    slug = models.CharField(
        unique=True,
        default=functools.partial(get_random_string, 12),
        max_length=12,
    )

    created = models.DateTimeField(default=datetime.datetime.utcnow)

    class Meta:
        ordering = ('created',)

    def __unicode__(self):
        return u"pk=%d type=%s phone_number=%r" % (
            self.pk,
            self.get_type_enum().name,
            self.phone_number,
        )

    @models.permalink
    def get_absolute_url(self):
        return 'reminders:logs:view', (self.slug,)

    def get_type_enum(self):
        return {x.value: x for x in TypeEnum}[self.type]

    def get_phone_number(self):
        """
        We store whatever number the user provided but massage it later.
        """
        return '+44%s' % self.phone_number if \
            self.phone_number.startswith('0') else self.phone_number

class Time(models.Model):
    """
    A time-of-day that this reminder should run.
    """

    reminder = models.ForeignKey('Reminder', related_name='times')

    time = models.CharField(max_length=5)
    last_run = models.DateTimeField(default=datetime.datetime.utcnow) # unused

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
    to be removed rather than marked as "disabled" which is complicated in the
    presence of ``unique_together``.
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
        default=functools.partial(get_random_string, 40),
        max_length=40,
    )

    # Nullable as failed requests would never see a SID
    twilio_sid = models.CharField(
        max_length=34,
        null=True,
        unique=True,
        default=None,
    )

    traceback = models.TextField()

    created = models.DateTimeField(default=datetime.datetime.utcnow)

    class Meta:
        abstract = True
        ordering = ('created',)
        get_latest_by = 'created'

    def __unicode__(self):
        return u"pk=%d instance_id=%d twilio_sid=%r state=%s" % (
            self.pk,
            self.instance_id,
            self.twilio_sid,
            self.get_state_enum().name,
        )

    @models.permalink
    def get_absolute_url(self):
        return 'reminders:%ss:status-callback' % self._meta.model_name, \
            (self.ident,)

    def get_state_enum(self):
        raise NotImplementedError()
