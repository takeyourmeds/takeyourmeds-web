from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.contrib import messages
from .models import Reminder

@login_required
def new_reminder(request):
    return render(request, 'new_reminder.html')


@login_required
def list_reminders(request):
    user = request.user
    return render(request, 'list_reminders.html', {
        'reminders': user.reminder_set.all().order_by('-pk'),
    })


@login_required
def delete_reminder(request, id):
    reminder = get_object_or_404(Reminder, pk=id)
    if(request.user.id == reminder.user_id):
        reminder.delete()
        messages.success(request, 'Your reminder has been deleted')
        return HttpResponseRedirect(reverse('reminder.views.list_reminders'))
    else:
        return HttpResponseForbidden('You do not own this reminder')


def send(request):
    if request.method == 'POST':
        return redirect('sent')
    return render(request, 'index.html')


def sent(request):
    return render(request, 'sent.html')
