from django.conf.urls import url, patterns

urlpatterns = patterns('takeyourmeds.reminder.views',
    url(r'^reminder/new$', 'new_reminder',
        name='new'),
    url(r'^reminder/list$', 'list_reminders',
        name='list'),
    url(r'^reminder/delete/(?P<id>\d+)/$', 'delete',
        name='delete'),
)
