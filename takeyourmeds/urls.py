from rest_framework import routers

from django.conf.urls import include, url

from takeyourmeds.api.views import ReminderViewSet

router = routers.DefaultRouter()
router.register(r'reminders', ReminderViewSet)

urlpatterns = [
    url(r'', include('takeyourmeds.api.urls')),
    url(r'', include('takeyourmeds.static.urls', namespace='static')),

    url('^telephony/', include("takeyourmeds.telephony.urls")),
    url('^reminder/', include("takeyourmeds.reminder.urls")),
    url(r'^api/', include(router.urls)),
    url(r'^accounts/', include('allauth.urls')),
]
