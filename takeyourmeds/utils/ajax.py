import json
import functools

from django.http import HttpResponse, HttpResponseBadRequest

class ajax(object):
    def __init__(self, login_required=False):
        self.login_required = login_required

    def __call__(self, fn):
        @functools.wraps(fn)
        def wrapped(request, *args, **kwargs):
            # @login_required returns a 30{1,2} redirect to some login page; we
            # want our Javascript applications to go down an "error" codepath
            # rather than try and parse the login page HTML, etc.
            if self.login_required and not request.user.is_authenticated():
                return HttpResponseBadRequest()

            response = fn(request, *args, **kwargs) or {}
            mimetype = 'text/html' if request.FILES else 'application/json'

            if isinstance(response, dict):
                return HttpResponse(
                    json.dumps(response),
                    content_type=mimetype,
                )

            return response
        return wrapped
