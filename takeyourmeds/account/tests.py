from takeyourmeds.utils.test import TestCase

class LoginTest(TestCase):
    def test_GET(self):
        """
        Can view the login page if logged out.
        """
        self.assertGET(200, 'account:login')

    def test_GET_logged_in(self):
        """
        Cannot view login page if you are logged in.
        """
        self.assertGET(302, 'account:login', login=True)

class LogoutTest(TestCase):
    def test_GET(self):
        """
        GET to logout asks for confirmation to avoid trivial CSRF.
        """
        self.assertGET(200, 'account:logout', login=True)

    def test_GET_logged_out(self):
        """
        GET to logout whilst logged-out redirects away.
        """
        self.assertGET(302, 'account:logout')

    def test_POST(self):
        """
        POST to logout whilst logged-in logs the user out.
        """
        self.assertPOST(302, {}, 'account:logout', login=True)

    def test_POST_logged_out(self):
        """
        POST to logout whilst logged-out logs redirects away.
        """
        self.assertPOST(302, {}, 'account:logout')
