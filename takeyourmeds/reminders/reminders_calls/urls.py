from django.conf.urls import url

from . import views

urlpatterns = (
    url(r'^_/status-callback/calls/(?P<ident>.+)$', views.status_callback,
        name='status-callback'),
)
