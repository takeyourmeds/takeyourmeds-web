from django.test import TestCase
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

class TestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            'testuser',
            'test@example.com',
            'password',
        )

    def assertStatusCode(self, status_code, fn, urlconf, *args, **kwargs):
        if kwargs.pop('login', False):
            self.client.login(username='testuser', password='password')

        response = fn(reverse(urlconf, args=args, kwargs=kwargs))

        self.assertEqual(response.status_code, status_code, response)

    def assertHTTP200(self, urlconf, *args, **kwargs):
        self.assertStatusCode(200, self.client.get, urlconf, *args, **kwargs)

    def assertHTTP302(self, urlconf, *args, **kwargs):
        self.assertStatusCode(302, self.client.get, urlconf, *args, **kwargs)

    def assertPOST(self, data, *args, **kwargs):
        status_code = kwargs.pop('status_code', 302)

        return self.assertStatusCode(
            status_code, lambda x: self.client.post(x, data), *args, **kwargs
        )

class SuperuserTestCase(TestCase):
    def setUp(self):
        super(SuperuserTestCase, self).setUp()

        self.user.is_superuser = True
        self.user.save()
