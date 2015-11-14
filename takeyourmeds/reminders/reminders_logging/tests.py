from takeyourmeds.utils.test import TestCase

from ..tasks import trigger_reminder

from .enums import StateEnum

class SmokeTest(TestCase):
    def test_success(self):
        instance = self.user.reminders.create(
            message='test',
        )
        self.assertEqual(instance.log_entries.count(), 0)

        trigger_reminder.delay(instance.pk)

        entry = instance.log_entries.get()

        self.assertEqual(entry.state, StateEnum.success)
        self.assertEqual(entry.traceback, "")
        self.assertNotEqual(entry.twilio_sid, "")

    def test_failure(self):
        instance = self.user.reminders.create()

        self.assertEqual(instance.log_entries.count(), 0)

        trigger_reminder.delay(instance.pk)

        entry = instance.log_entries.get()

        self.assertEqual(entry.state, StateEnum.error)
        self.assertNotEqual(entry.traceback, "")
