from takeyourmeds.utils.test import TestCase

class SmokeTest(TestCase):
    def test_landing(self):
        self.assertGET(200, 'static:landing')

    def test_landing_logged_in(self):
        response = self.assertGET(302, 'static:landing', login=True)
        self.assertRedirectsTo(response, 'dashboard:view')

    def test_about(self):
        self.assertGET(200, 'static:about')

    def test_faq(self):
        self.assertGET(200, 'static:faq')

    def test_contact(self):
        self.assertGET(200, 'static:contact')

    def test_terms_and_conditions(self):
        self.assertGET(200, 'static:terms')

    def test_privacy_policy(self):
        self.assertGET(200, 'static:privacy')

class HTTPTest(TestCase):
    def test_404(self):
        self.assertGET(200, 'static:http-404')

    def test_500(self):
        self.assertGET(200, 'static:http-500')

class AdminTest(TestCase):
    def test_admin_logged_out(self):
        self.assertGET(302, 'static:admin')

    def test_admin_regular_user(self):
        self.assertGET(302, 'static:admin', login=True)

    def test_admin_superuser(self):
        self.user.is_superuser = True
        self.user.save()

        self.assertGET(200, 'static:admin', login=True)
