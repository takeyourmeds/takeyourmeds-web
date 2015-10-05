from django_auto_one_to_one import PerUserData

from django.db import models

from .utils import get_default_group

class UserData(PerUserData('profile')):
    group = models.ForeignKey(
        'groups.Group',
        related_name='users',
        default=get_default_group,
    )
