"""
This file must be kept up-to-date with Stripe, especially the slugs:

  https://manage.stripe.com/plans
"""

BY_SLUG = {}
BY_VALUE = {}

class Plan(object):
    def __init__(self, value, slug, display):
        self.value = value
        self.slug = slug
        self.display = display

        BY_SLUG[slug] = self
        BY_VALUE[value] = self

FREE = Plan(1, 'free', "Free plan")
