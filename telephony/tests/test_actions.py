import unittest

from django.conf import settings
from django.test import TestCase
from django.test.utils import override_settings

from telephony import actions

@override_settings(TWILIO_CONFIG=settings.TWILIO_CONFIGS.get('test'))
@unittest.skipIf('test' not in settings.TWILIO_CONFIGS, "Missing test config")
class TestActions(TestCase):

    def test_call(self):
        sid = actions.make_call(
            "+441324430099",
            "https://api.twilio.com/cowbell.mp3"
        )
        assert len(sid) == 34

    def test_sms(self):
        sid = actions.send_sms("+441324430099", "Hello!")
        assert len(sid) == 34

