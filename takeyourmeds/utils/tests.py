import re
import os

from django.core import checks
from django.conf import settings

from .test import TestCase

re_url = re.compile(r'\shref="(?P<url>(?!https?:|mailto:|{|#)[^"]*)"')

class TestTemplates(TestCase):
    def assertValidURLs(self, filename):
        with open(filename) as f:
            urls = [m.group('url') for m in re_url.finditer(f.read())]

        self.failIf(urls, "%s contains hardcoded URLs: %r" % (
            filename,
            urls,
        ))

    idx = 0
    for x in settings.TEMPLATES:
        for y in x['DIRS']:
            for root, _, filenames in os.walk(y):
                for z in filenames:
                    def wrapper(self, filename=os.path.join(root, z)):
                        self.assertValidURLs(filename)
                    idx += 1
                    locals()['test_template_idx_%04d' % idx] = wrapper
