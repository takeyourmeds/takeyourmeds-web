from django.conf.urls import url, patterns

urlpatterns = patterns('takeyourmeds.reminder.views',
    url(r'^new/$', 'new_reminder',
        name='reminder_new'),
    url(r'^list/$', 'list_reminders',
        name='list-reminders'),
)
