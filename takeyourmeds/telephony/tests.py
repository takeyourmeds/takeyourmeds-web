from takeyourmeds.utils.test import TestCase

from .actions import make_call, send_sms

class TestActions(TestCase):
    def test_call(self):
        sid = make_call('+441324430099', 'https://api.twilio.com/cowbell.mp3')

        self.assertEqual(len(sid), 34)

    def test_sms(self):
        sid = send_sms('+441324430099', "Hello!")

        self.assertEqual(len(sid), 34)

