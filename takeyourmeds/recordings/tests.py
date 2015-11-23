from takeyourmeds.utils.test import TestCase

class SmokeTest(TestCase):
    def setUp(self):
        super(SmokeTest, self).setUp()

    def test_view(self):
        self.assertHTTP200('recordings:view')