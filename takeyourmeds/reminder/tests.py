import pytz
import datetime

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
