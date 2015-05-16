import datetime

import pytz
from django.test import TestCase

from .models import Reminder

class TestCron(TestCase):
    def test_cron(self):

        ten_min_ago = datetime.datetime.now(pytz.utc) - datetime.timedelta(minutes=10)
        r = Reminder(
            crontab="* * * * *",
            message="test",
            phone_number="123",
            last_run=ten_min_ago,
        )
        r.save()
        if r.should_run():
            task.run(r)
            r.last_run = now
