import pytz
import datetime

from django.core.urlresolvers import reverse

from takeyourmeds.utils.test import TestCase

class TestCron(TestCase):
    def test_cron(self):
        ten_min_ago = datetime.datetime.now(pytz.utc) - \
            datetime.timedelta(minutes=10)

        reminder = self.user.reminders.create(
            message="test",
            telnumber='123',
        )

        reminder.times.create(
            cronstring="* * * * *",
            last_run=ten_min_ago,
        )

    def test_delete(self):
        r = self.user.reminders.create()
        url = reverse('reminder:delete', args=(r.pk,))
        self.client.delete(url, format='json')

    def test_cannot_delete_other_users_reminder(self):
        r = self.user.reminders.create()
        url = reverse('reminder:delete', args=(r.pk,))
        self.client.delete(url, format='json')
