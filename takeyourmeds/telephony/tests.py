from takeyourmeds.utils.test import TestCase

from .utils import make_call
from .models import TwilioMLCallback

class TestActions(TestCase):
    def test_call(self):
        sid = make_call('+441324430099', 'https://api.twilio.com/cowbell.mp3').sid

        self.assertEqual(len(sid), 34)
        self.assert_(TwilioMLCallback.objects.all()[0].get_callback_url())
