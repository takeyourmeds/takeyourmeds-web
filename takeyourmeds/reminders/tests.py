import datetime

from takeyourmeds.utils.test import TestCase

class SmokeTest(TestCase):
    def test_index(self):
        self.assertGET(200, 'reminders:index', login=True)

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
        self.assertRedirectsTo(response, 'reminders:index')
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

class TestCron(TestCase):
    def test_cron(self):
        ten_min_ago = datetime.datetime.utcnow() - \
            datetime.timedelta(minutes=10)

        reminder = self.user.reminders.create(
            message="test",
            telnumber='123',
        )

        reminder.times.create(
            cronstring="* * * * *",
            last_run=ten_min_ago,
        )

class TriggerTest(TestCase):
    def test_trigger_now(self):
        instance = self.user.reminders.create()

        response = self.assertPOST(
            302,
            {},
            'reminders:trigger', instance.pk,
            login=True,
        )

        self.assertRedirectsTo(response, 'reminders:index')
