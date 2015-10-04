from takeyourmeds.utils.test import TestCase

class SmokeTest(TestCase):
    def test_landing(self):
        self.assertGET(200, 'static:landing')

    def test_landing_logged_in(self):
        response = self.assertGET(302, 'static:landing', login=True)
        self.assertRedirectsTo(response, 'reminders:index')

    def test_about(self):
        self.assertGET(200, 'static:about')

    def test_terms_and_conditions(self):
        self.assertGET(200, 'static:terms')

    def test_privacy_policy(self):
        self.assertGET(200, 'static:privacy')
