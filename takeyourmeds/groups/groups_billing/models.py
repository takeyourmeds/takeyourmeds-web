from django.db import models

from django_auto_one_to_one import AutoOneToOneModel

from ..models import Group

from .plans import PLANS, FREE

class Billing(AutoOneToOneModel(Group)):
    plan = models.IntegerField(
        choices=sorted((x.value, x.display) for x in PLANS.values()),
        default=FREE.value,
    )
