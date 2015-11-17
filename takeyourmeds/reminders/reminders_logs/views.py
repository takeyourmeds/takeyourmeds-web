from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

@login_required
def view(request, slug):
    reminder = get_object_or_404(request.user.reminders, slug=slug)

    template = 'reminders/logs/%s.html' % reminder.get_type_enum().name

    return render(request, template, {
        'reminder': reminder,
    })
