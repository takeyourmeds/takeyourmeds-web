import urlparse

from django.conf import settings
from django.core.urlresolvers import reverse

def reverse_absolute(urlconf, *args, **kwargs):
    return urlparse.urljoin(
        settings.SITE_URL,
        reverse(urlconf, *args, **kwargs),
    )
