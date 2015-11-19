from django.db import models

from takeyourmeds.utils.url import resolve_absolute

from ..models import AbstractNotification

from .enums import StateEnum

class Call(AbstractNotification):
    state = models.IntegerField(
        default=StateEnum.dialing.value,
        choices=[(x.value, x.name) for x in StateEnum],
    )

    def get_state_enum(self):
        return {x.value: x for x in StateEnum}[self.state]
