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
    call = get_object_or_404(Call, ident=ident)
    call.state = StateEnum.answered # FIXME
    call.save()

    return HttpResponse('')
