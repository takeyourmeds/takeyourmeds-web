import stripe

from django.db import models

class GroupManager(models.Manager):
    def create_group(self, *args, **kwargs):
        """
        Create a Group, ensuring Stripe is correctly configured. This is the
        only entry point for creating group instances.
        """

        stripe_kwargs = kwargs.pop('stripe_kwargs')

        # Create the actual group
        group = self.create(*args, **kwargs)

        # Configure Stripe
        customer = stripe.Customer.create(**stripe_kwargs)

        group.billing.stripe_customer_ident = customer.id
        group.billing.save(update_fields=('stripe_customer_ident',))
        group.billing.sync()

        return group
