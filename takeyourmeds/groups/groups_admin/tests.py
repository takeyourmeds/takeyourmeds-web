from takeyourmeds.utils.test import SuperuserTestCase

class SmokeTest(SuperuserTestCase):
    def test_index(self):
        self.assertGET(200, 'groups:admin:index', login=True)

    def test_view(self):
        self.assertGET(
            200,
            'groups:admin:view',
            self.user.profile.group_id,
            login=True,
        )
