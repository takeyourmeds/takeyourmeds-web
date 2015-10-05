from django_auto_one_to_one import AutoOneToOneModel

from ..models import Group

class Billing(AutoOneToOneModel(Group)):
    pass
