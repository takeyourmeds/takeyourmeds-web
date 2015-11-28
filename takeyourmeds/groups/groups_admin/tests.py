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

    def test_create_access_tokens(self):
        group = self.user.profile.group

        self.assertEqual(group.access_tokens.count(), 0)

        self.assertPOST(
            302,
            {'num_tokens': 10},
            'groups:admin:create-access-tokens',
            group.pk,
            login=True,
        )

        self.assertEqual(group.access_tokens.count(), 10)
