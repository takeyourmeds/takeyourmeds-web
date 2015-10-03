from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def new_reminder(request):
    return render(request, 'reminder/new_reminder.html')

@login_required
def list_reminders(request):
    reminders = request.user.reminder_set.order_by('-pk')

    return render(request, 'reminder/list_reminders.html', {
        'reminders': reminders,
    })

def send(request):
    if request.method == 'POST':
        return redirect('sent')
    return render(request, 'reminder/index.html')

def sent(request):
    return render(request, 'reminder/sent.html')
