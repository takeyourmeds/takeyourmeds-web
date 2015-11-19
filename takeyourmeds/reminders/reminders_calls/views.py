import datetime

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from ..tasks import trigger_instance

from . import app_settings
from .enums import StateEnum
from .models import Call

@csrf_exempt
@require_POST
def twiml_callback(request, ident):
    call = get_object_or_404(Call, ident=ident)

    return render(request, 'reminders/calls/twiml_callback.xml', {
        'call': call,
    }, content_type='text/xml')

@csrf_exempt
@require_POST
def gather_callback(request, ident):
    call = get_object_or_404(Call, ident=ident)

    # Mark if the user actually pressed a button
    if request.POST.get('Digits'):
        call.button_pressed = datetime.datetime.utcnow()
        call.save(update_fields=('button_pressed',))

    return HttpResponse("")

@csrf_exempt
@require_POST
def status_callback(request, ident):
    """
    https://www.twilio.com/help/faq/voice/what-do-the-call-statuses-mean

    Example POST data:

        SipResponseCode: 500
        ApiVersion: 2010-04-01
        AccountSid: AC7d6b676d2a17527a71a2bb41301b5e6f
        Duration: 0
        Direction: outbound-api
        CallStatus: busy
        SequenceNumber: 0
        Timestamp: Mon, 16 Nov 2015 16:10:53 +0000
        Caller: +441143032046
        CallDuration: 0
        To: +447753237119
        CallbackSource: call-progress-events
        Called: +447751231511
        From: +441143032046
        CallSid: CA19fd373bd82b81b602c75d1ddc7745e7
    """

    call = get_object_or_404(Call, ident=ident)

    try:
        call.state = {
            'queued': StateEnum.dialing,
            'initiated': StateEnum.dialing,
            'ringing': StateEnum.dialing,
            'in-progress': StateEnum.answered,
            'completed': StateEnum.answered,
            'busy': StateEnum.busy,
            'no-answer': StateEnum.no_answer,
            'cancelled': StateEnum.failed,
            'failed': StateEnum.failed,
        }[request.POST['CallStatus']]
    except KeyError:
        call.state = StateEnum.unknown

    call.state_updated = datetime.datetime.utcnow()

    call.save(update_fields=('state', 'state_updated'))

    if not call.button_pressed \
            and call.instance.calls.count() < app_settings.RETRY_COUNT:
        trigger_instance.delay(call.instance_id)

    return HttpResponse('')
