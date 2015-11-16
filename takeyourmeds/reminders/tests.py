from takeyourmeds.utils.test import TestCase

class SmokeTest(TestCase):
    def test_create(self):
        self.assertGET(200, 'reminders:create', login=True)

class DeleteTests(TestCase):
    def test_GET(self):
        instance = self.user.reminders.create()
        self.assertGET(405, 'reminders:delete', instance.pk, login=True)

    def test_POST(self):
        instance = self.user.reminders.create()
        self.assert_(self.user.reminders.exists())
        response = self.assertPOST(
            302, {}, 'reminders:delete', instance.pk, login=True
        )
        self.assertRedirectsTo(response, 'dashboard:view')
        self.failIf(self.user.reminders.exists())

    def test_forbidden(self):
        """
        Users cannot delete other user's reminders.
        """

        other = self.create_user('other')
        instance = self.user.reminders.create()

        self.assertPOST(
            404,
            {},
            'reminders:delete',
            instance.pk,
            login=True,
            user=other,
        )

        self.assert_(self.user.reminders.exists())

class TriggerTest(TestCase):
    def test_trigger_now(self):
        reminder = self.user.reminders.create(
            message="test",
            phone_number='123',
        )

        response = self.assertPOST(
            302,
            {},
            'reminders:trigger', reminder.pk,
            login=True,
        )

        self.assertRedirectsTo(response, 'dashboard:view')

        instance = reminder.instances.get()
        message = instance.messages.get()

        self.assert_(message.twilio_sid)
