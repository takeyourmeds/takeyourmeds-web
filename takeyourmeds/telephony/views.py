import os
import json

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from . import actions


def info(request, uuid):
    """
    Return the Twillio ML that we generated when the user
    called /call
    """
    data = open(os.path.join("/tmp", uuid + ".xml")).read()
    return HttpResponse(data, content_type="text/xml")

