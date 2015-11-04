from django_auto_one_to_one import AutoOneToOneModel

from django.db import models

from takeyourmeds.account.models import User

from .utils import get_default_group

class UserData(AutoOneToOneModel(User, related_name='profile')):
    group = models.ForeignKey(
        'groups.Group',
        related_name='users',
    )

    def save(self, *args, **kwargs):
        # Cannot use default= as  the check framework evaluates them before the
        # database is guaranteed to be consistent.
        if self.group_id is None:
            self.group = get_default_group()

        super(UserData, self).save(*args, **kwargs)
