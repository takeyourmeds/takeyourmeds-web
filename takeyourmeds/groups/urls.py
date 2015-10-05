from django.conf.urls import patterns, url

urlpatterns = patterns('takeyourmeds.groups.views',
    (r'', include('takeyourmeds.groups.groups_admin.urls', namespace='admin')),
    (r'', include('takeyourmeds.groups.groups_billing.urls', namespace='billing')),
)
