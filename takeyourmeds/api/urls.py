from rest_framework import routers

from django.conf.urls import url, patterns, include

from takeyourmeds.api.views import ReminderViewSet

router = routers.DefaultRouter()
router.register(r'reminders', ReminderViewSet)

urlpatterns = patterns('takeyourmeds.api.views',
    url(r'^api/trigger/$', 'trigger_now',
        name='trigger-now'),

    url(r'', include(router.urls)),
)
