from django.test import TestCase
from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse

User = get_user_model()

class TestCase(TestCase):
    def setUp(self):
        self.user = self.create_user('testuser')

    def assertStatusCode(self, status_code, fn, urlconf, *args, **kwargs):
        if kwargs.pop('login', False):
            user = kwargs.pop('user', self.user)
            self.client.login(email=user.email, password='password')

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

    def assertRedirectsTo(self, response, urlconf, *args, **kwargs):
        status_code = kwargs.pop('status_code', 302)
        target_status_code = kwargs.pop('target_status_code', 200)

        return self.assertRedirects(
            response,
            reverse(urlconf, args=args, kwargs=kwargs),
            status_code,
            target_status_code,
        )

    def create_user(self, email):
        return User.objects.create_user(email, 'password')

class SuperuserTestCase(TestCase):
    def setUp(self):
        super(SuperuserTestCase, self).setUp()

        self.user.is_staff = True
        self.user.is_superuser = True
        self.user.save()
