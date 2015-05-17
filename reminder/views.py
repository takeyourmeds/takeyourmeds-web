from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


@login_required
def new_reminder(request):
    return render(request, 'new_reminder.html')


@login_required
def list_reminders(request):
    user = request.user
    return render(request, 'list_reminders.html', {
        'reminders': user.reminder_set.all().order_by('-pk'),
    })


def send(request):
    if request.method == 'POST':
        return redirect('sent')
    return render(request, 'index.html')


def sent(request):
    return render(request, 'sent.html')
