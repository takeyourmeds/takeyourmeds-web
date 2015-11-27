from takeyourmeds.utils.test import TestCase

from .models import Group

class SmokeTest(TestCase):
    def test_token(self):
        self.user.profile.group.access_tokens.create()
