from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.contrib import messages

from .models import Reminder

@login_required
def new_reminder(request):
    return render(request, 'reminder/new_reminder.html')

@login_required
def list_reminders(request):
    reminders = request.user.reminders.order_by('-pk')

    return render(request, 'reminder/list_reminders.html', {
        'reminders': reminders,
    })

@login_required
def delete(request, id):
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
    return render(request, 'reminder/index.html')

def sent(request):
    return render(request, 'reminder/sent.html')
