import urlparse

from django.conf import settings
from django.core.urlresolvers import reverse

def reverse_absolute(target, *args, **kwargs):
    if not target.startswith('/'):
        target = reverse(target, *args, **kwargs)

    return urlparse.urljoin(settings.SITE_URL, target)
