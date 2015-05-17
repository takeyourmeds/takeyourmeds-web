from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase

class AccountTests(APITestCase):
    def test_create_reminder(self):
        url = reverse('reminder-list')
        data = {
            'message': 'lorem',
            'audiourl': '',
            'telnumber': '123',
            'reminder_times': [
                u'0 7 * * *',
                u'30 12 * * *',
                u'45 8 * * *',
            ]
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, data)