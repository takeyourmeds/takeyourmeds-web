import datetime

import pytz
from django.test import TestCase

from reminder.models import Reminder, ReminderTime


class TestCron(TestCase):
    def test_cron(self):

        ten_min_ago = (
            datetime.datetime.now(pytz.utc) -
            datetime.timedelta(minutes=10)
        )
        r = Reminder(
            message="test",
            telnumber="123",
        )
        r.save()

        rt = ReminderTime(
            cronstring="* * * * *",
            last_run=ten_min_ago,
            reminder=r,
        )
        rt.save()
