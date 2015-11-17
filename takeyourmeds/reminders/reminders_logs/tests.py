from takeyourmeds.utils.test import TestCase

from ..enums import TypeEnum, SourceEnum

class SmokeTest(TestCase):
    def setUp(self):
        super(SmokeTest, self).setUp()

        self.reminder = self.user.reminders.create(
            type=TypeEnum.message,
        )

        self.reminder.instances.create(
            source=SourceEnum.manual,
        ).messages.create()

    def test_view(self):
        self.assertGET(200, 'reminders:logs:view', self.reminder.pk, login=True)
