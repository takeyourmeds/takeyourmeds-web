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
        self.assertEqual(self.user.recording_create_requests.count(), 0)
        self.assertCreate({'phone_number': '07751234567'}, 'success')
        self.assertEqual(self.user.recording_create_requests.count(), 1)
        self.assertEqual(self.user.recordings.count(), 0)

    def test_poll_creates_in_tests(self):
        url = self.assertCreate(
            {'phone_number': '07751234567'},
            'success',
        ).json()['url']

        data = self.assertPOST(200, {}, url, login=True).json()

        recording = self.user.recordings.get()

        self.assertEqual(
            self.user.recording_create_requests.get().recording_id,
            recording.pk,
        )
        self.assertEqual(data, {
            'status': 'success',
            'recording_id': recording.pk,
        })

    def test_twiml_callback(self):
        self.assertCreate({'phone_number': '07751234567'}, 'success')

        create_request = self.user.recording_create_requests.get()

        self.assertPOST(
            200,
            {},
            'recordings:create:twiml-callback',
            create_request.ident,
        )

    def test_record_callback(self):
        self.assertCreate({'phone_number': '07751234567'}, 'success')

        create_request = self.user.recording_create_requests.get()

        self.assertPOST(
            200,
            {'RecordingUrl': '/'},
            'recordings:create:record-callback',
            create_request.ident,
        )

        self.assertEqual(self.user.recordings.get().audio_file.size, 0)

    def test_record_callback_missing_recording_url(self):
        self.assertCreate({'phone_number': '07751234567'}, 'success')

        create_request = self.user.recording_create_requests.get()

        self.assertPOST(
            400,
            {},
            'recordings:create:record-callback',
            create_request.ident,
        )
