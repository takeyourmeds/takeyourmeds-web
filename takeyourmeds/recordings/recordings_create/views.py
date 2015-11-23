import urllib

from django.http import HttpResponseBadRequest
from django.shortcuts import get_object_or_404, render
from django.core.files import File
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from takeyourmeds.utils.ajax import ajax

from .forms import CreateForm
from .models import CreateRequest

@require_POST
@ajax(login_required=True)
def xhr_create(request):
    form = CreateForm(request.POST)

    if not form.is_valid():
        return {
            'status': 'error',
            'errors': [form.errors.values()],
        }

    instance = form.save(request.user)

    return {
        'status': 'success',
        'url': reverse('recordings:create:xhr-poll', args=(instance.ident,)),
    }

@require_POST
@ajax(login_required=True)
def xhr_poll(request, ident):
    create_request = get_object_or_404(
        request.user.recording_create_requests,
        ident=ident,
    )

    if create_request.recording_id is None:
        return {'status': 'continue'}

    return {
        'status': 'success',
        'recording_id': create_request.recording_id,
    }

@csrf_exempt
@require_POST
def twiml_callback(request, ident):
    create_request = get_object_or_404(CreateRequest, ident=ident)

    return render(request, 'reminders/calls/audio/twiml_callback.xml', {
        'create_request': create_request,
    }, content_type='text/xml')

@csrf_exempt
@require_POST
def record_callback(request, ident):
    create_request = get_object_or_404(CreateRequest, ident=ident)

    recording_url = request.POST.get('RecordingUrl', '')

    if not recording_url:
        return HttpResponseBadRequest("Could not find RecordingUrl")

    # "A request to the RecordingUrl will return a recording in binary WAV
    # audio format by default. To request the recording in MP3 format, append
    # ".mp3" to the RecordingUrl."
    filename, _ = urllib.urlretrieve('%s.mp3' % recording_url)

    with open(filename) as f:
        recording = create_request.user.recordings.create(
            create_request=create_request,
        )
        recording.recording.save(File(f))

    return render(
        request,
        'reminders/calls/audio/record_callback.xml',
        content_type='text/xml'
    )
