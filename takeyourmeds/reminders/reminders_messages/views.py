from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_POST

from .enums import StateEnum
from .models import Message

@require_POST
def status_callback(twilio_sid):
    message = get_object_or_404(Message, twilio_sid=twilio_sid)
    message.state = StateEnum.delivered # FIXME
    message.save()

    return HttpResponse('')
