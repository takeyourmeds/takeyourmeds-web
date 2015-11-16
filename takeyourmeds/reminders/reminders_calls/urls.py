from django.conf.urls import url

from . import views

urlpatterns = (
    url(r'^_/status-callback/calls/(?P<twilio_sid>.+)$', views.status_callback,
        name='status-callback'),
)
