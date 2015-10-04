from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    reminders = request.user.reminders.order_by('-pk')

    return render(request, 'reminders/index.html', {
        'reminders': reminders,
    })

@login_required
def create(request):
    return render(request, 'reminders/create.html')

@require_POST
@login_required
def delete(request, reminder_id):
    instance = get_object_or_404(request.user.reminders, pk=reminder_id)
    instance.delete()

    messages.success(request, "Your reminder has been deleted.")

    return redirect('reminders:index')

@require_POST
@login_required
def trigger(request, reminder_id):
    instance = get_object_or_404(request.user.reminders, pk=reminder_id)
    instance.dispatch_task()

    messages.success(request, "Your reminder has been triggered.")

    return redirect('reminders:index')
