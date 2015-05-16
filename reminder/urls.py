from django.conf.urls import patterns, include, url
from rest_framework import routers

from .api import ReminderViewSet

router = routers.DefaultRouter()
router.register(r'reminders', ReminderViewSet)


urlpatterns = patterns(
    '',
    url(r'', include(router.urls)),
)
