from django.test import TestCase
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

class TestCase(TestCase):
    def setUp(self):
        self.user = self.create_user('testuser')

    def assertStatusCode(self, status_code, fn, urlconf, *args, **kwargs):
        if kwargs.pop('login', False):
            user = kwargs.pop('user', self.user)
            self.client.login(username=user.username, password='password')

        response = fn(reverse(urlconf, args=args, kwargs=kwargs))

        self.assertEqual(
            response.status_code,
            status_code,
            "Got HTTP %d but expected HTTP %d. Response:\n%s" % (
                response.status_code,
                status_code,
                response,
            )
        )

        return response

    def assertGET(self, status_code, urlconf, *args, **kwargs):
        return self.assertStatusCode(
            status_code,
            self.client.get,
            urlconf,
            *args,
            **kwargs
        )

    def assertPOST(self, status_code, data, *args, **kwargs):
        return self.assertStatusCode(
            status_code, lambda x: self.client.post(x, data), *args, **kwargs
        )

    def assertPOSTRedirects(self, data, *args, **kwargs):
        status_code = kwargs.pop('status_code', 302)
        expected_url = reverse(
            kwargs.pop('target'),
            args=kwargs.pop('target_args', ()),
            kwargs=kwargs.pop('target_kwargs', {})
        )

        response = self.assertStatusCode(
            status_code, lambda x: self.client.post(x, data), *args, **kwargs
        )

        self.assertRedirects(response, expected_url, status_code)

        return response

    def create_user(self, username):
        return User.objects.create_user(
            username,
            '%s@example.org' % username,
            'password',
        )

class SuperuserTestCase(TestCase):
    def setUp(self):
        super(SuperuserTestCase, self).setUp()

        self.user.is_staff = True
        self.user.is_superuser = True
        self.user.save()
