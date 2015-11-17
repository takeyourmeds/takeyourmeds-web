from django.db import models

from ..models import AbstractNotification

from .enums import StateEnum

class Message(AbstractNotification):
    state = models.IntegerField(
        default=StateEnum.sending.value,
        choices=[(x.value, x.name) for x in StateEnum],
    )

    def get_state_enum(self):
        return {x.value: x for x in StateEnum}[self.state]
