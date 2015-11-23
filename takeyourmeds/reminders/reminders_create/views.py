from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.core.urlresolvers import reverse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required

from takeyourmeds.utils.ajax import ajax, get_form_errors

from .forms import CreateForm, CreateRecordRequestForm

@login_required
def view(request):
    if request.method == 'POST':
        form = CreateForm(request.POST)

        if form.is_valid():
            form.save(request.user)

            messages.success(
                request,
                "Your reminder has been created.",
            )

            return redirect('dashboard:view')
    else:
        form = CreateForm()

    return render(request, 'reminders/create/view.html', {
        'form': form,
    })

@require_POST
@ajax(login_required=True)
def xhr_record_request_create(request):
    form = CreateRecordRequestForm(request.POST)

    if not form.is_valid():
        return {
            'status': 'error',
            'errors': get_form_errors(form),
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
def xhr_record_request_poll(request, ident):
    record_request = get_object_or_404(
        request.user.audio_recording_requests,
        ident=ident,
    )

    # FIXME
    if record_request:
        pass

    return {'status': 'continue'}
