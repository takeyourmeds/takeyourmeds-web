from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.contrib.staticfiles.storage import staticfiles_storage

from takeyourmeds.utils.url import reverse_absolute

from ..tasks import trigger_instance

from . import app_settings
from .enums import StateEnum
from .models import Call

def twiml_callback(request, ident):
    call = get_object_or_404(Call, ident=ident)

    absolute_audio_url = reverse_absolute(
        staticfiles_storage.url(call.instance.reminder.audio_url),
    )

    return HttpResponse("""
        <?xml version="1.0" encoding="UTF-8"?>
        <Response>
            <Play loop="1">{}</Play>
        </Response>
    """.format(absolute_audio_url).strip())

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

    call.save()

    if call.state in (
        StateEnum.failed,
        StateEnum.busy,
        StateEnum.no_answer,
    ) and call.instance.calls.count() < app_settings.RETRY_COUNT:
        trigger_instance.delay(call.instance_id)

    return HttpResponse('')
