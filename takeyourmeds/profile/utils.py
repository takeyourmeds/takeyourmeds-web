from takeyourmeds.groups.models import Group

def get_default_group():
    """
    To avoid a NULL field and to simplify Stripe integration, we assign users
    to a "catch-all" group by default.

    We create it if it doesn't exist. This ensures we don't need "test
    fixtures" for the live site.
    """

    return Group.objects.get_or_create(
        name="Legacy/catch-all group",
    )[0]

