from django.conf.urls import url

from . import views

urlpatterns = (
    url(r'^reminders/create$', views.view,
        name='view'),

    url(r'^xhr/reminders/create/create-record-request$', views.xhr_record_request_create,
        name='xhr-record-request-create'),
    url(r'^xhr/reminders/create/poll-record-request$', views.xhr_record_request_poll,
        name='xhr-record-request-poll'),
)
