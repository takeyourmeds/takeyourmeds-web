from takeyourmeds.groups.models import Group
from takeyourmeds.groups.groups_billing.plans import PLANS

def get_default_group():
    """
    To avoid a NULL field and to simplify Stripe integration, we assign users
    to a "catch-all" group by default.

    We create it if it doesn't exist. This ensures we don't need "test
    fixtures" for the live site.
    """

    name = "Legacy/catch-all group"

    try:
        return Group.objects.get(name=name)
    except Group.DoesNotExist:
        return Group.objects.create_group(
            name="Legacy/catch-all group",
            stripe_kwargs={
                'plan': PLANS['free'].slug,
            },
        )
