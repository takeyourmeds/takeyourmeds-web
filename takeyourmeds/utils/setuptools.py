import os
import unittest

class TestSuite(unittest.TestSuite):
    def run(self, *args, **kwargs):
        assert os.system('takeyourmeds/manage.py test --verbosity=2') == 0
