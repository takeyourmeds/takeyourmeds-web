from takeyourmeds.utils.test import TestCase

class SmokeTest(TestCase):
    def test_index(self):
        self.assertGET(200, 'dashboard:view', login=True)
