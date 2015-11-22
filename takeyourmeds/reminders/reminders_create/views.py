from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse
from django.views.decorators.http import require_POST

from takeyourmeds.utils.ajax import ajax

from .forms import CreateRecordRequestForm

@require_POST
@ajax(login_required=True)
def xhr_record_request_create(request):
    form = CreateRecordRequestForm(request.POST)

    if not form.is_valid():
        return {'errors': {
            x: y.get_json_data() for x, y in form.errors.items()
        }}

    record_request = form.save(request.user)

    url = reverse(
        'reminders:create:xhr-record-request-poll',
        args=(record_request.ident,),
    )

    return {'url': url}

@require_POST
@ajax(login_required=True)
def xhr_record_request_poll(request, ident):
    record_request = get_object_or_404(
        request.user.audio_recording_requests,
        ident=ident,
    )

    # FIXME
    if record_request:
        pass

    return {'status': 'continue'}
