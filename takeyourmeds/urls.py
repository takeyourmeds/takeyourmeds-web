from django.conf import settings
from django.conf.urls import include, url
from django.views.static import serve

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
)

if settings.DEBUG:
    urlpatterns += (
        url(r'^storage/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    )
