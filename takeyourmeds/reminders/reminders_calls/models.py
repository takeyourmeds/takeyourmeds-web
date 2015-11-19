from django.db import models

from ..models import AbstractNotification

from .enums import StateEnum

class Call(AbstractNotification):
    state = models.IntegerField(
        default=StateEnum.dialing.value,
        choices=[(x.value, x.name) for x in StateEnum],
    )

    button_pressed = models.DateTimeField(null=True, default=None)

    def get_state_enum(self):
        return {x.value: x for x in StateEnum}[self.state]
