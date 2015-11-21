from django.conf.urls import url

from . import views

urlpatterns = (
    url(r'^_/reminders/calls/audio/twiml/(?P<ident>\w{40})$', views.twiml_callback,
        name='twiml-callback'),
    url(r'^_/reminders/calls/audio/twiml/(?P<ident>\w{40})$', views.record_callback,
        name='record-callback'),
)
