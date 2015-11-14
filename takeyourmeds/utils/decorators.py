from django.conf import settings
from django.contrib.auth.decorators import user_passes_test

logout_required = user_passes_test(
    lambda x: not x.is_authenticated(),
    settings.LOGIN_REDIRECT_URL,
)

superuser_required = user_passes_test(lambda u: (u.is_authenticated() and u.is_superuser))
