from takeyourmeds.utils.test import TestCase

from ..tasks import trigger_reminder

from .enums import StateEnum

class SmokeTest(TestCase):
    def test_success(self):
        reminder = self.user.reminders.create(message='test')
        self.assertEqual(reminder.instances.count(), 0)
        trigger_reminder.delay(reminder.pk)

        instance = reminder.instances.get()

        self.assertEqual(instance.get_state_enum(), StateEnum.success)
        self.assertEqual(instance.traceback, "")
        self.assertNotEqual(instance.twilio_sid, "")

    def test_failure(self):
        reminder = self.user.reminders.create()
        self.assertEqual(reminder.instances.count(), 0)
        trigger_reminder.delay(reminder.pk)

        instance = reminder.instances.get()

        self.assertEqual(instance.get_state_enum(), StateEnum.error)
        self.assert_(instance.traceback)
