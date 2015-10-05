from takeyourmeds.utils.test import SuperuserTestCase

class SmokeTest(SuperuserTestCase):
    def test_index(self):
        self.assertGET(200, 'groups:admin:index', login=True)
