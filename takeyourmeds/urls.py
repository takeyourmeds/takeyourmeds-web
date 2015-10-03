from django.conf.urls import include, url

urlpatterns = (
    url(r'', include('takeyourmeds.api.urls', namespace='api')),
    url(r'', include('takeyourmeds.reminder.urls', namespace='reminder')),
    url(r'', include('takeyourmeds.static.urls', namespace='static')),
    url(r'', include('takeyourmeds.telephony.urls', namespace='telephony')),

    url(r'^accounts/', include('allauth.urls')),
)
