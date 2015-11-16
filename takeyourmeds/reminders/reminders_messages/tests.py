from takeyourmeds.utils.test import TestCase

from ..enums import TypeEnum, SourceEnum

from .enums import StateEnum

class StatusCallbackTest(TestCase):
    def setUp(self):
        super(StatusCallbackTest, self).setUp()

        self.message = self.user.reminders.create(
            type=TypeEnum.message,
        ).instances.create(
            source=SourceEnum.manual,
        ).messages.create()

    def assertState(self, val, expected):
        self.assertPOST(200, {'MessageStatus': val}, self.message)
        self.message.refresh_from_db()
        self.assertEqual(self.message.state, expected)

    def test_sending(self):
        self.assertState('accepted', StateEnum.sending)
        self.assertState('queued', StateEnum.sending)
        self.assertState('sending', StateEnum.sending)

    def test_sent(self):
        self.assertState('sent', StateEnum.sent)

    def test_delivered(self):
        self.assertState('delivered', StateEnum.delivered)

    def test_failed(self):
        self.assertState('failed', StateEnum.failed)
        self.assertState('undelivered', StateEnum.failed)

    def test_unknown(self):
        self.assertState('dummy-unknown-value', StateEnum.unknown)
