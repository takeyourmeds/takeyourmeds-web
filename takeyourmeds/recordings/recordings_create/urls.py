from django.conf.urls import url

from . import views

urlpatterns = (
    url(r'^_/recordings/create$', views.xhr_create,
        name='xhr-create'),
    url(r'^_/recordings/create/poll/(?P<ident>\w{40})$', views.xhr_poll,
        name='xhr-poll'),

    url(r'^_/recordings/create/twiml-callback/(?P<ident>\w{40})$', views.twiml_callback,
        name='twiml-callback'),
    url(r'^_/recordings/create/record-callback/(?P<ident>\w{40})$', views.record_callback,
        name='record-callback'),
)
