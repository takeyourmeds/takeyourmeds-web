from takeyourmeds.groups.models import Group
from takeyourmeds.groups.groups_billing.plans import BY_SLUG

def get_default_group():
    """
    To avoid a NULL field and to simplify Stripe integration, we assign users
    to a "catch-all" group by default.

    We create it if it doesn't exist. This ensures we don't need "test
    fixtures" for the live site.
    """

    group, created = Group.objects.get_or_create(
        name="Legacy/catch-all group",
    )

    if created:
        group.billing.create_stripe_customer(plan=BY_SLUG['free'].slug)

    return group
