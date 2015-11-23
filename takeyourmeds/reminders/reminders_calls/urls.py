from django.conf.urls import url

from . import views

urlpatterns = (
    url(r'^_/twiml-callback/calls/(?P<ident>\w{40})$', views.twiml_callback,
        name='twiml-callback'),
    url(r'^_/gather-callback/calls/(?P<ident>\w{40})$', views.gather_callback,
        name='gather-callback'),
    url(r'^_/status-callback/calls/(?P<ident>\w{40})$', views.status_callback,
        name='status-callback'),
)
