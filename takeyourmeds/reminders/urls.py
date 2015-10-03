from django.conf.urls import url, patterns

urlpatterns = patterns('takeyourmeds.reminders.views',
    url(r'^reminders$', 'index',
        name='index'),
    url(r'^reminders/new$', 'create',
        name='create'),
    url(r'^reminders/reminder/(?P<reminder_id>\d+)/delete$', 'delete',
        name='delete'),
)
