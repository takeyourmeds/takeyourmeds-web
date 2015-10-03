from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from .models import TwilioMLCallback

def callback(request, ident):
    """
    Return the Twillio ML that we generated when the user called /call
    """

    instance = get_object_or_404(TwilioMLCallback, ident=ident)

    return HttpResponse(instance.content, content_type='text/xml')
