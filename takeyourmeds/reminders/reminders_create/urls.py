from django.conf.urls import url

from . import views

urlpatterns = (
    url(r'^xhr/reminders/create-record-request$', views.xhr_create_record_request,
        name='xhr-create-record-request'),
)
