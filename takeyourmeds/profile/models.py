from django_auto_one_to_one import PerUserData

from django.db import models

class UserData(PerUserData('profile')):
    group = models.ForeignKey(
        'groups.Group',
        null=True,
        related_name='users',
    )
