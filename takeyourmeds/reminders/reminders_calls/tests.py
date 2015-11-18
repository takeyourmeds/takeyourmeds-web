from django.conf import settings

from takeyourmeds.utils.test import TestCase

from ..enums import TypeEnum, SourceEnum

from .enums import StateEnum

class CallTestCase(TestCase):
    def setUp(self):
        super(CallTestCase, self).setUp()

        self.reminder = self.user.reminders.create(
            type=TypeEnum.call,
            audio_url='/dummy.mp3',
        )

        self.call = self.reminder.instances.create(
            source=SourceEnum.manual,
        ).calls.create()

class TwimlCallbackTest(CallTestCase):
    def assertContains(self, expected):
        response = self.assertGET(
            200,
            'reminders:calls:twiml-callback',
            self.call.ident,
        )

        self.assert_(expected in response.content)

    def test_url(self):
        url = self.call.get_twiml_callback_url()

        self.assert_(url.startswith('http'))

    def test_xml(self):
        """
        Is actually an XML document.
        """
        self.assertContains('<?xml')

    def test_absolute_url(self):
        """
        Audio URL is absolute.
        """
        self.assertContains(settings.SITE_URL)

    def test_audio_url(self):
        """
        XML contains our audio URL
        """
        self.assertContains(self.reminder.audio_url)

class StatusCallbackTest(CallTestCase):
    def assertState(self, val, expected):
        self.assertPOST(200, {'CallStatus': val}, self.call)
        self.call.refresh_from_db()
        self.assertEqual(self.call.state, expected)

    def test_dialing(self):
        self.assertState('queued', StateEnum.dialing)
        self.assertState('initiated', StateEnum.dialing)
        self.assertState('ringing', StateEnum.dialing)

    def test_answered(self):
        self.assertState('in-progress', StateEnum.answered)
        self.assertState('completed', StateEnum.answered)

    def test_busy(self):
        self.assertState('busy', StateEnum.busy)

    def test_no_answer(self):
        self.assertState('no-answer', StateEnum.no_answer)

    def test_failed(self):
        self.assertState('failed', StateEnum.failed)
        self.assertState('cancelled', StateEnum.failed)

    def test_unknown(self):
        self.assertState('dummy-unknown-value', StateEnum.unknown)

class RetryTest(TestCase):
    def test_retry(self):
        instance = self.user.reminders.create(
            type=TypeEnum.call,
            audio_url='/dummy.mp3',
        ).instances.create(
            source=SourceEnum.manual,
        )

        # Initiate the first call manually
        call = instance.calls.create()

        # First call is busy
        call = instance.calls.latest()
        print call.pk
        self.assertEqual(instance.calls.count(), 1)
        self.assertPOST(200, {'CallStatus': 'busy'}, call)
        call.refresh_from_db()
        self.assertEqual(call.state, StateEnum.busy)

        # This would have caused us to schedule another call automatically
        call = instance.calls.latest()
        self.assertEqual(instance.calls.count(), 2)
        self.assertEqual(call.state, StateEnum.dialing)

        # .. which is also busy
        self.assertPOST(200, {'CallStatus': 'busy'}, call)
        call.refresh_from_db()
        self.assertEqual(call.state, StateEnum.busy)
