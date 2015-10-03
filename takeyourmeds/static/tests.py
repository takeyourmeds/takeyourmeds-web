from takeyourmeds.utils.test import TestCase

class SmokeTest(TestCase):
    def test_landing(self):
        self.assertHTTP200('static:landing')

    def test_about(self):
        self.assertHTTP200('static:about')

    def test_terms_and_conditions(self):
        self.assertHTTP200('static:terms')

    def test_privacy_policy(self):
        self.assertHTTP200('static:privacy')
