from django.contrib.auth.models import User

from takeyourmeds.utils.test import TestCase

class RegistrationTest(TestCase):
    def test_GET(self):
        """
        Logged-out users can view the registration page.
        """
        self.assertGET(200, 'registration:view')

    def test_POST(self):
        num_users = User.objects.count()

        self.assertPOST(302, {
            'username': 'test',
            'password': 'password',
            'email': 'test@example.org',
        }, 'registration:view')

        self.assertEqual(User.objects.count(), num_users + 1)

    def test_POST_logged_in(self):
        """
        Cannot register if you are logged in.
        """
        num_users = User.objects.count()
        self.assertPOST(302, {}, 'registration:view', login=True)
        self.assertEqual(User.objects.count(), num_users)

    def test_GET_logged_in(self):
        """
        Redirect away if viewing the register page when logged in.
        """
        self.assertGET(302, 'registration:view', login=True)
