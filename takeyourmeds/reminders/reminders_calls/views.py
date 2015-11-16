from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_POST

from .enums import StateEnum
from .models import Call

@require_POST
def status_callback(twilio_sid):
    call = get_object_or_404(Call, twilio_sid=twilio_sid)
    call.state = StateEnum.answered # FIXME
    call.save()

    return HttpResponse('')
