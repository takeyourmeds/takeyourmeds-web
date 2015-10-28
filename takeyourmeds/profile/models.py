from django_auto_one_to_one import AutoOneToOneModel

from django.db import models

from takeyourmeds.account.models import User

from .utils import get_default_group

class UserData(AutoOneToOneModel(User)):
    group = models.ForeignKey(
        'groups.Group',
        related_name='users',
        default=get_default_group,
    )
