from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

@login_required
def new(request):
    return render(request, 'reminder/new_reminder.html')

@login_required
def list_(request):
    reminders = request.user.reminders.order_by('-pk')

    return render(request, 'reminder/list_reminders.html', {
        'reminders': reminders,
    })

@login_required
def delete(request, reminder_id):
    """
    FIXME: @require_POST
    """

    reminder = get_object_or_404(request.user.reminders, pk=reminder_id)
    reminder.delete()

    messages.success(request, "Your reminder has been deleted.")

    return redirect('reminders:list')

def send(request):
    if request.method == 'POST':
        return redirect('sent')
    return render(request, 'reminder/index.html')

def sent(request):
    return render(request, 'reminder/sent.html')
