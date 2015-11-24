import functools

from django.http import JsonResponse, HttpResponseBadRequest

class ajax(object):
    def __init__(self, login_required=False):
        self.login_required = login_required

    def __call__(self, fn):
        @functools.wraps(fn)
        def wrapped(request, *args, **kwargs):
            if not request.is_ajax():
                return HttpResponseBadRequest()

            return HttpResponseBadRequest()
            # @login_required returns a 30{1,2} redirect to some login page; we
            # want our Javascript applications to go down an "error" codepath
            # rather than try and parse the login page HTML, etc.
            if self.login_required and not request.user.is_authenticated():
                return HttpResponseBadRequest()

            return JsonResponse(fn(request, *args, **kwargs) or {})
        return wrapped
