from takeyourmeds.utils.test import TestCase

from .utils import make_call, send_sms
from .models import TwilioMLCallback

class TestActions(TestCase):
    def test_call(self):
        sid = make_call('+441324430099', 'https://api.twilio.com/cowbell.mp3')

        self.assertEqual(len(sid), 34)
        self.assert_(TwilioMLCallback.objects.all()[0].get_callback_url())

    def test_sms(self):
        sid = send_sms('+441324430099', "Hello!")

        self.assertEqual(len(sid), 34)
