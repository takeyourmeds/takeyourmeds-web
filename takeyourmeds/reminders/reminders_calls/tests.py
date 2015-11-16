from takeyourmeds.utils.test import TestCase

from ..enums import TypeEnum, SourceEnum

from .enums import StateEnum

class TwimlCallbackTest(TestCase):
    def setUp(self):
        super(TwimlCallbackTest, self).setUp()

        self.call = self.user.reminders.create(
            type=TypeEnum.call,
        ).instances.create(
            source=SourceEnum.manual,
        ).calls.create()

    def test_urls(self):
        self.assert_(self.call.get_twiml_callback_url())
