from django.conf import settings

def settings_context(request):
    """
    Expose the settings directly in the template. This is preferable to
    site_context etc.
    """

    return {'settings': settings}
