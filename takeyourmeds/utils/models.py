import stripe

from django.conf import settings
from django.template.base import add_to_builtins

add_to_builtins('django.contrib.staticfiles.templatetags.staticfiles')

stripe.api_key = settings.STRIPE_SECRET_KEY

if not settings.STRIPE_ENABLED:
    def instance(**attrs):
        return type('_instance', (object,), attrs)

    class Subscription(object):
        def __init__(self, id):
            self.plan = instance(id=id)

    class Subscriptions(object):
        def all(self, *args, **kwargs):
            return instance(data=[Subscription('free')])

    class Customer(object):
        def __init__(self, id):
            self.id = id

        subscriptions = Subscriptions()

    def create(cls, *args, **kwargs):
        return Customer(123)

    def retrieve(cls, ident):
        return Customer(ident)

    stripe.Customer.create = classmethod(create)
    stripe.Customer.retrieve = classmethod(retrieve)
