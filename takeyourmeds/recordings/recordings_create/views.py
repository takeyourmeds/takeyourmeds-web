import urllib

from django.http import HttpResponseBadRequest
from django.shortcuts import get_object_or_404, render
from django.core.files import File
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.core.urlresolvers import reverse
from django.views.decorators.http import require_POST

from takeyourmeds.utils.ajax import ajax

from .forms import CreateForm
from .models import RecordRequest

@require_POST
@ajax(login_required=True)
def xhr_create(request):
    form = CreateForm(request.POST)

    if not form.is_valid():
        return {
            'status': 'error',
            'errors': [' '.join(y) for _, y in form.errors.items()],
        }

    record_request = form.save(request.user)

    url = reverse(
        'reminders:create:xhr-record-request-poll',
        args=(record_request.ident,),
    )

    return {
        'status': 'success',
        'url': url,
    }

@require_POST
@ajax(login_required=True)
def xhr_poll(request, ident):
    record_request = get_object_or_404(
        request.user.audio_record_requests,
        ident=ident,
    )

    if record_request.recording_id is None:
        return {'status': 'continue'}

    return {
        'status': 'success',
        'recording_id': record_request.recording_id,
    }

@csrf_exempt
@require_POST
def twiml_callback(request, ident):
    record_request = get_object_or_404(RecordRequest, ident=ident)

    return render(request, 'reminders/calls/audio/twiml_callback.xml', {
        'record_request': record_request,
    }, content_type='text/xml')

@csrf_exempt
@require_POST
def record_callback(request, ident):
    record_request = get_object_or_404(RecordRequest, ident=ident)

    recording_url = request.POST.get('RecordingUrl', '')

    if not recording_url:
        return HttpResponseBadRequest("Could not parse RecordingUrl in output")

    # "A request to the RecordingUrl will return a recording in binary WAV
    # audio format by default. To request the recording in MP3 format, append
    # ".mp3" to the RecordingUrl."
    filename, _ = urllib.urlretrieve('%s.mp3' % recording_url)

    with open(filename) as f:
        recording = record_request.user.recordings.create(
            record_request=record_request,
        )
        recording.recording.save(File(f))

    return render(
        request,
        'reminders/calls/audio/record_callback.xml',
        content_type='text/xml'
    )
