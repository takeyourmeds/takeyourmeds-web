from django.conf.urls import patterns, include, url
from rest_framework import routers

from .api import ReminderViewSet

router = routers.DefaultRouter()
router.register(r'reminders', ReminderViewSet)

from reminder.views import new_reminder, send, sent

urlpatterns = patterns(
    '',
    url(r'^new$',new_reminder, name="reminder_new" ),
    url(r'', include(router.urls)),
)
