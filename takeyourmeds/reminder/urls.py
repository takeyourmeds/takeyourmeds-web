from django.conf.urls import url

from .api import trigger_now
from .views import new_reminder, list_reminders

urlpatterns = (
    url(r'^new/$', new_reminder,
        name='reminder_new'),
    url(r'^list/$', list_reminders,
        name='list-reminders'),
    url(r'^trigger/$', trigger_now,
        name='trigger_now'),
)
