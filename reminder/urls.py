from django.conf.urls import url

from reminder.views import new_reminder

urlpatterns = [
    url(r'^new/$', new_reminder, name="reminder_new" ),
]
