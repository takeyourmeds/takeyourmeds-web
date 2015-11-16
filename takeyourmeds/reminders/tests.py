from takeyourmeds.utils.test import TestCase

from .enums import TypeEnum

class SmokeTest(TestCase):
    def test_create(self):
        self.assertGET(200, 'reminders:create', login=True)

class DeleteTests(TestCase):
    def setUp(self):
        super(DeleteTests, self).setUp()

        self.reminder = self.user.reminders.create(type=TypeEnum.message)

    def test_GET(self):
        self.assertGET(405, 'reminders:delete', self.reminder.pk, login=True)

    def test_POST(self):
        response = self.assertPOST(
            302, {}, 'reminders:delete', self.reminder.pk, login=True
        )
        self.assertRedirectsTo(response, 'dashboard:view')
        self.failIf(self.user.reminders.exists())

    def test_forbidden(self):
        """
        Users cannot delete other user's reminders.
        """

        other = self.create_user('other')

        self.assertPOST(
            404,
            {},
            'reminders:delete',
            self.reminder.pk,
            login=True,
            user=other,
        )

        self.assert_(self.user.reminders.exists())

class TriggerTest(TestCase):
    def test_trigger_now(self):
        reminder = self.user.reminders.create(type=TypeEnum.message)

        response = self.assertPOST(
            302,
            {},
            'reminders:trigger', reminder.pk,
            login=True,
        )

        self.assertRedirectsTo(response, 'dashboard:view')

        message = reminder.instances.get().messages.get()

        self.assert_(message.twilio_sid)
