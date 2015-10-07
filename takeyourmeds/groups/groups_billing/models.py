import stripe

from django.db import models

from django_auto_one_to_one import AutoOneToOneModel

from ..models import Group

from .plans import PLANS

class Billing(AutoOneToOneModel(Group)):
    stripe_customer_ident = models.CharField(unique=True, max_length=255)

    plan = models.IntegerField(
        choices=sorted((x.value, x.display) for x in PLANS.values()),
        default=PLANS['free'].value,
    )

    def get_plan_object(self):
        return PLANS[self.plan]

    def get_stripe_customer(self):
        return stripe.Customer.retrieve(self.stripe_customer_ident)

    def sync(self):
        customer = self.get_stripe_customer()

        for x in customer.subscriptions.all(count=1).data:
            self.plan = PlANS[x.plan.id].value

        self.save(update_fields=('plan',))
