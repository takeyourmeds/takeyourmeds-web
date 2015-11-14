from takeyourmeds.utils.test import TestCase

from ..tasks import trigger_reminder

from .enums import StateEnum

class SmokeTest(TestCase):
    def test_success(self):
        instance = self.user.reminders.create(
            message='test',
        )
        self.assertEqual(instance.instances.count(), 0)

        trigger_reminder.delay(instance.pk)

        entry = instance.instances.get()

        self.assertEqual(entry.get_state_enum(), StateEnum.success)
        self.assertEqual(entry.traceback, "")
        self.assertNotEqual(entry.twilio_sid, "")

    def test_failure(self):
        instance = self.user.reminders.create()

        self.assertEqual(instance.instances.count(), 0)

        trigger_reminder.delay(instance.pk)

        entry = instance.instances.get()

        self.assertEqual(entry.get_state_enum(), StateEnum.error)
        self.assertNotEqual(entry.traceback, "")
