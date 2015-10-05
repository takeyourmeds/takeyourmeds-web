from django.conf.urls import patterns, include

urlpatterns = patterns('takeyourmeds.groups.views',
    (r'', include('takeyourmeds.groups.groups_admin.urls', namespace='admin')),
)
