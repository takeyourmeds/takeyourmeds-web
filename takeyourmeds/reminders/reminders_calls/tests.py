from django.conf import settings

from takeyourmeds.utils.test import TestCase

from ..enums import TypeEnum, SourceEnum

from .enums import StateEnum

class TwimlCallbackTest(TestCase):
    def setUp(self):
        super(TwimlCallbackTest, self).setUp()

        self.reminder = self.user.reminders.create(
            type=TypeEnum.call,
            audio_url='/dummy.mp3',
        )

        self.call = self.reminder.instances.create(
            source=SourceEnum.manual,
        ).calls.create()

    def test_url(self):
        url = self.call.get_twiml_callback_url()

        self.assert_(url.startswith('http'))

    def test_content(self):
        response = self.assertGET(
            200,
            'reminders:calls:twiml-callback',
            self.call.ident,
        )

        self.assert_(response.content.startswith('<?xml'))
        self.assert_(settings.SITE_URL in response.content)
        self.assert_(self.reminder.audio_url in response.content)
