from django.conf.urls import url, patterns

urlpatterns = patterns('takeyourmeds.reminders.views',
    url(r'^reminders/new$', 'create',
        name='create'),
    url(r'^reminders/reminder/(?P<reminder_id>\d+)/delete$', 'delete',
        name='delete'),
    url(r'^reminders/reminder/(?P<reminder_id>\d+)/trigger$', 'trigger',
        name='trigger'),
)
