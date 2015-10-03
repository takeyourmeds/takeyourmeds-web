from django.conf.urls import url, patterns

urlpatterns = patterns('takeyourmeds.reminders.views',
    url(r'^reminder/new$', 'new',
        name='new'),
    url(r'^reminder/list$', 'list_',
        name='list'),
    url(r'^reminder/delete/(?P<reminder_id>\d+)$', 'delete',
        name='delete'),
)
