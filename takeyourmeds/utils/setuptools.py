import os
import unittest

class TestSuite(unittest.TestSuite):
    def run(self, *args, **kwargs):
        assert os.system('%(_)s takeyourmeds/manage.py test --verbosity=2' % os.environ) == 0
