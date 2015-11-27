import datetime
import functools

from django.db import models
from django.utils.crypto import get_random_string

from .managers import GroupManager

class Group(models.Model):
    """
    Instances must be created using ``Group.objects.create_group`` to ensure
    Stripe is configured correctly.
    """

    name = models.CharField(max_length=255, unique=True)

    created = models.DateTimeField(default=datetime.datetime.utcnow)

    objects = GroupManager()

    class Meta:
        ordering = ('-created',)
        get_latest_by = 'created'

    def __unicode__(self):
        return u"#%d: %s (%s)" % (
            self.pk,
            self.name,
            self.slug,
        )

class Token(models.Model):
    group = models.ForeignKey(Group, related_name='tokens')

    token = models.CharField(
        unique=True,
        max_length=8,
        default=functools.partial(get_random_string, 8, 'ACEFHKJMLNPRUTWVYX'),
    )

    user = models.OneToOneField(
        'account.User',
        null=True,
        related_name='token',
    )

    created = models.DateTimeField(default=datetime.datetime.utcnow)

    class Meta:
        ordering = ('-created',)
        get_latest_by = 'created'

    def __unicode__(self):
        return u"group_id=%r token=%r user_id=%s" % (
            self.group_id,
            self.token,
            self.user_id,
        )
