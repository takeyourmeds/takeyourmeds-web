from rest_framework import routers

from django.conf.urls import include, url

from takeyourmeds.api.views import ReminderViewSet

router = routers.DefaultRouter()
router.register(r'reminders', ReminderViewSet)

urlpatterns = (
    url(r'', include('takeyourmeds.api.urls', namespace='api')),
    url(r'', include('takeyourmeds.reminder.urls', namespace='reminder')),
    url(r'', include('takeyourmeds.static.urls', namespace='static')),
    url(r'', include('takeyourmeds.telephony.urls', namespace='telephony')),

    url(r'^accounts/', include('allauth.urls')),
    url(r'^api/', include(router.urls)),
)
