import os
import json

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

import actions

def info(request, uuid):
    """
    Return the Twillio ML that we generated when the user
    called /call
    """
    data = open(os.path.join("/tmp", uuid + ".xml")).read()
    return HttpResponse(data, content_type="text/xml")


@csrf_exempt
def make_call(request):
    incoming = json.loads(request.body)
    to_number = incoming['to']
    message_url = incoming["message_url"]

    incoming["id"] = actions.make_call(to_number, message_url)
    return HttpResponse(json.dumps(incoming), content_type='application/json')

@csrf_exempt
def send_sms(request):
    incoming = json.loads(request.body)
    incoming["id"] = actions.send_sms(incoming['to'], incoming['message'])
    return HttpResponse(json.dumps(incoming), content_type='application/json')