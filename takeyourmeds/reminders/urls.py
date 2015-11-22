from django.conf.urls import url, include

from . import views

urlpatterns = (
    url(r'', include('takeyourmeds.reminders.reminders_calls.urls',
        namespace='calls')),
    url(r'', include('takeyourmeds.reminders.reminders_create.urls',
        namespace='create')),
    url(r'', include('takeyourmeds.reminders.reminders_logs.urls',
        namespace='logs')),
    url(r'', include('takeyourmeds.reminders.reminders_messages.urls',
        namespace='messages')),

    url(r'^reminders/reminder/(?P<slug>[^/]+)/delete$', views.delete,
        name='delete'),
    url(r'^reminders/reminder/(?P<slug>[^/]+)/trigger$', views.trigger,
        name='trigger'),
)
