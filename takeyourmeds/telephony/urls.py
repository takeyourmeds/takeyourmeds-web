from django.conf.urls import url

from .views import info

urlpatterns = (
    url('^info/(?P<uuid>.*)$', info,
        name='info'),
)
