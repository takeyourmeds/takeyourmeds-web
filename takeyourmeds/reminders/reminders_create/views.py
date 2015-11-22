from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from reminders.utils.ajax import ajax

@ajax(login_required=True)
def xhr_create_record_request(request):
    record_request = 

    return render(request, 'reminders/create/view.html', {
        'record_
    })
