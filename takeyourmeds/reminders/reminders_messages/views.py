from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from .enums import StateEnum
from .models import Message

@csrf_exempt
@require_POST
def status_callback(request, ident):
    """
    https://www.twilio.com/help/faq/sms/what-do-the-sms-statuses-mean

    Example POST fields:

        ApiVersion: 2010-04-01
        AccountSid: AC7d6b676d2a17527a71a2bb41301b5e6f
        SmsSid: SMaff4a74e3fe241b3b35f84ccf5130d50
        From: TakeYourMed
        MessageSid: SMaff4a74e3fe241b3b35f84ccf5130d50
        SmsStatus: sent
        MessageStatus: sent
        To: +447490416163
    """

    message = get_object_or_404(Message, ident=ident)

    try:
        message.state = {
            'accepted': StateEnum.sending,
            'queued': StateEnum.sending,
            'sending': StateEnum.sending,
            'sent': StateEnum.sent,
            'delivered': StateEnum.delivered,
            'failed': StateEnum.failed,
            'undelivered': StateEnum.failed,
        }[request.POST['MessageStatus']]
    except KeyError:
        message.state = StateEnum.unknown

    message.save()

    return HttpResponse('')
