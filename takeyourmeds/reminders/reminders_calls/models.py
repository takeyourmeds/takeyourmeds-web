import urlparse

from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse

from ..models import AbstractNotification

from .enums import StateEnum

class Call(AbstractNotification):
    state = models.IntegerField(
        default=StateEnum.in_progress.value,
        choices=[(x.value, x.name) for x in StateEnum],
    )

    def get_state_enum(self):
        return {x.value: x for x in StateEnum}[self.state]

    def get_twiml_callback_url(self):
        return urlparse.urljoin(
            settings.SITE_URL,
            reverse('reminders:calls:twiml-callback', args=(self.ident,)),
        )
