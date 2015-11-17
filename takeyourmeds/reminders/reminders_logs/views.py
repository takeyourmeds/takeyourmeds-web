from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

@login_required
def view(request, reminder_id):
    reminder = get_object_or_404(request.user.reminders, pk=reminder_id)

    template = 'reminders/logs/%s.html' % reminder.get_type_enum().name

    return render(request, template, {
        'reminder': reminder,
    })
