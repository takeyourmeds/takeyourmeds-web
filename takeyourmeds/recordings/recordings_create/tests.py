from takeyourmeds.utils.test import TestCase

class CreateTest(TestCase):
    def assertCreate(self, data, status):
        response = self.assertPOST(
            200,
            data,
            'recordings:create:xhr-create',
            login=True,
        )

        self.assertEqual(response.json()['status'], status)

        return response

    def test_missing(self):
        self.assertCreate({}, 'error')

    def test_invalid(self):
        self.assertCreate({'phone_number': 'invalid'}, 'error')

    def test_create(self):
        self.assertCreate({'phone_number': '07751234567'}, 'success')

    def test_poll(self):
        response = self.assertCreate({'phone_number': '07751234567'}, 'success')

        url = response.json()['url']

        self.assertPOST(200, {}, url, login=True)
