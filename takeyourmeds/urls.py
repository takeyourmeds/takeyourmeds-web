from django.conf.urls import include, url

urlpatterns = (
    url(r'', include('takeyourmeds.account.urls',
        namespace='account')),
    url(r'', include('takeyourmeds.dashboard.urls',
        namespace='dashboard')),
    url(r'', include('takeyourmeds.groups.urls',
        namespace='groups')),
    url(r'', include('takeyourmeds.registration.urls',
        namespace='registration')),
    url(r'', include('takeyourmeds.reminders.urls',
        namespace='reminders')),
    url(r'', include('takeyourmeds.static.urls',
        namespace='static')),
    url(r'', include('takeyourmeds.telephony.urls',
        namespace='telephony')),
)
