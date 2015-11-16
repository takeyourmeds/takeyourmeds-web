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
