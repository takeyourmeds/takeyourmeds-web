import re
import os

from django.core import checks
from django.conf import settings

re_url = re.compile(r'\shref="(?P<url>/[^"]*)"')

@checks.register()
def hardcoded_urls(app_configs, **kwargs):
    for x in settings.TEMPLATES:
        for y in x['DIRS']:
            for root, _, filenames in os.walk(y):
                for z in filenames:
                    fullpath = os.path.join(root, z)

                    with open(fullpath) as f:
                        html = f.read()

                    for m in re_url.finditer(html):
                        yield checks.Error("%s contains hardcoded URL %r" % (
                            fullpath,
                            m.group('url'),
                        ), id='takeyourmeds.utils.E001')
