import stripe

from django.db import models

from django_auto_one_to_one import AutoOneToOneModel

from ..models import Group

from .plans import BY_SLUG, BY_VALUE

class Billing(AutoOneToOneModel(Group)):
    stripe_customer_ident = models.CharField(unique=True, max_length=255)

    plan = models.IntegerField(
        choices=sorted((x.value, x.display) for x in BY_SLUG.values()),
        default=BY_SLUG['free'].value,
    )

    def get_plan_object(self):
        return BY_VALUE[self.plan]

    def get_stripe_customer(self):
        return stripe.Customer.retrieve(self.stripe_customer_ident)

    def sync_from_stripe(self):
        customer = self.get_stripe_customer()

        for x in customer.subscriptions.all(count=1).data:
            self.plan = PlANS[x.plan.id].value

        self.save(update_fields=('plan',))
