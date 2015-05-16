from django.test import Client, TestCase
import json
import requests

class TestTelephony(TestCase):

    def setup(self):
        self.client = Client()

    def test_call(self):
        d = {
            # Who to call
            "to": "+447472785934",
            # URL or the MP3 to play
            "message_url": "https://api.twilio.com/cowbell.mp3"
        }

        response = self.client.post("/telephony/call", json.dumps(d), content_type="application/json")


    def test_sms(self):
        d = {
            # Who to call
            "to": "+447472785934",
            # What to send
            "message": "This is a message"
        }

        response = self.client.post("/telephony/sms", json.dumps(d), content_type="application/json")

        result = json.loads(response.content)
        for k, v in result.iteritems():
            if k == 'id':
                continue
            assert result[k] == d[k]