from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.test import APITestCase

class ReminderTests(APITestCase):
    def setUp(self):
        self.u = User.objects.create(username='test')
        self.u2 = User.objects.create(username='test2')

    def test_create_reminder(self):
        self.client.force_authenticate(user=self.u)
        url = reverse('reminder-list')
        data = {
            'message': 'lorem',
            'audiourl': '',
            'telnumber': '123',
            'times': [
                '0 7 * * *',
                '30 12 * * *',
                '45 8 * * *',
            ],
        }

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, data)

    def test_create_reminder_for_user(self):
        self.client.force_authenticate(user=self.u2)
        url = reverse('reminder-list')
        data = {
            'message': 'lorem',
            'audiourl': '',
            'telnumber': '123',
            'times': [
                u'0 7 * * *',
                u'30 12 * * *',
                u'45 8 * * *',
            ],
        }

        # Make 3 objects
        self.client.post(url, data, format='json')
        self.client.post(url, data, format='json')
        self.client.post(url, data, format='json')

        res = self.client.get(url)
        self.assertEqual(len(res.data), 3)

        self.client.logout()

        res = self.client.get(url)
        self.assertEqual(len(res.data), 1)

    def test_trigger_now(self):
        self.u.reminders.create()
        url = reverse('api:trigger-now')
        self.client.post(url, {'id': 1}, format='json')
