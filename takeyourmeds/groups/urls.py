from django.conf.urls import url, include

urlpatterns = (
    url(r'', include('takeyourmeds.groups.groups_admin.urls', namespace='admin')),
)
