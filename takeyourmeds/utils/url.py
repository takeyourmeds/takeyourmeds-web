import urlparse

from django.conf import settings
from django.shortcuts import resolve_url

def resolve_absolute(*args, **kwargs):
    return urlparse.urljoin(settings.SITE_URL, resolve_url(*args, **kwargs))
