from django.core import mail

from takeyourmeds.utils.test import TestCase

class ResetPasswordTest(TestCase):
    def test_view(self):
        self.assertGET(200, 'account:forgot-password:view')

    def test_post(self):
        response = self.assertPOST(
            302,
            {'email': self.user.email},
            'account:forgot-password:view',
            login=False,
        )

        self.assertEqual(len(mail.outbox), 1)
        self.assertRedirectsTo(response, 'account:forgot-password:view')
