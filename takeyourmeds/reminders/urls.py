from django.conf.urls import url

from . import views

urlpatterns = (
    url(r'^reminders/new$', views.create,
        name='create'),
    url(r'^reminders/reminder/(?P<reminder_id>\d+)/delete$', views.delete,
        name='delete'),
    url(r'^reminders/reminder/(?P<reminder_id>\d+)/trigger$', views.trigger,
        name='trigger'),
)
