from django.conf.urls import include, url

urlpatterns = (
    url(r'', include('takeyourmeds.api.urls', namespace='api')),
    url(r'', include('takeyourmeds.reminders.urls', namespace='reminders')),
    url(r'', include('takeyourmeds.static.urls', namespace='static')),
    url(r'', include('takeyourmeds.telephony.urls', namespace='telephony')),

    url(r'^accounts/', include('allauth.urls')),
)
