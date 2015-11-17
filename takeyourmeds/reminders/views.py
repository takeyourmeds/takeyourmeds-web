from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required

from .forms import CreateForm
from .tasks import trigger_reminder

@login_required
def create(request):
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

    return render(request, 'reminders/create.html', {
        'form': form,
    })

@require_POST
@login_required
def delete(request, slug):
    instance = get_object_or_404(request.user.reminders, slug=slug)
    instance.delete()

    messages.success(request, "Your reminder has been deleted.")

    return redirect('dashboard:view')

@require_POST
@login_required
def trigger(request, slug):
    instance = get_object_or_404(request.user.reminders, slug=slug)

    trigger_reminder.delay(instance.pk)

    messages.info(request, "A test for your reminder has been triggered.")

    return redirect('dashboard:view')
