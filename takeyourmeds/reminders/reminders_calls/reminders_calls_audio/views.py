import datetime

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from ..tasks import trigger_instance

from .models import Request

@csrf_exempt
@require_POST
def twiml_callback(request, ident):
    call = get_object_or_404(Call, ident=ident)

    return render(request, 'reminders/calls/twiml_callback.xml', {
        'call': call,
    }, content_type='text/xml')

@csrf_exempt
@require_POST
def record_callback(request, ident):
    call = get_object_or_404(Call, ident=ident)

    # Mark if the user actually pressed a button
    if request.POST.get('Digits'):
        call.button_pressed = datetime.datetime.utcnow()
        call.save(update_fields=('button_pressed',))

    return render(
        request,
        'reminders/calls/gather_callback.xml',
        content_type='text/xml'
    )
