from takeyourmeds.utils.test import TestCase

class SmokeTest(TestCase):
    def test_token(self):
        self.user.profile.group.access_tokens.create()
