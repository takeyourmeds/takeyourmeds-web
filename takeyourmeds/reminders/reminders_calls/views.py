import urlparse

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib.staticfiles.storage import staticfiles_storage

from .enums import StateEnum
from .models import Call

def twiml_callback(request, ident):
    call = get_object_or_404(Call, ident=ident)

    absolute_audio_url = urlparse.urljoin(
        settings.SITE_URL,
        staticfiles_storage.url(call.instance.reminder.audio_url),
    )

    return HttpResponse("""
        <?xml version="1.0" encoding="UTF-8"?>
        <Response>
            <Play loop="1">{}</Play>
        </Response>
    """.format(absolute_audio_url).strip())

@require_POST
def status_callback(request, ident):
    """
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
            'busy': StateEnum.busy,
        }[request.POST['CallStatus']]
    except KeyError:
        call.state = StateEnum.unknown

    call.save()

    return HttpResponse('')
