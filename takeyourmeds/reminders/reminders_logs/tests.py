from takeyourmeds.utils.test import TestCase

from ..enums import TypeEnum, SourceEnum

class SmokeTest(TestCase):
    def create_reminder(self, type):
        reminder = self.user.reminders.create(type=type)

        reminder.instances.create(
            source=SourceEnum.manual,
        ).messages.create()

        return reminder

    def test_call(self):
        reminder = self.create_reminder(TypeEnum.call)

        self.assertGET(200, reminder, login=True)

    def test_message(self):
        reminder = self.create_reminder(TypeEnum.message)

        self.assertGET(200, reminder, login=True)
