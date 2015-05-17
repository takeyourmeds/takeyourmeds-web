from django.conf.urls import url

from reminder.views import new_reminder, list_reminders
from reminder.api import trigger_now

urlpatterns = [
    url(r'^new/$', new_reminder, name="reminder_new"),
    url(r'^list/$', list_reminders, name="list-reminders" ),
    url(r'^trigger/$', trigger_now, name="trigger_now"),
]
