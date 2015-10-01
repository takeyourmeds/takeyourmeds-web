import os

from django.http import HttpResponse

def info(request, uuid):
    """
    Return the Twillio ML that we generated when the user called /call
    """

    with open(os.path.join('/tmp', '%s.xml' % uuid)) as f:
        data = f.read()

    return HttpResponse(data, content_type='text/xml')
