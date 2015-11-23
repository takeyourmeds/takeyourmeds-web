from django.conf.urls import url, include

urlpatterns = (
    url(r'', include('takeyourmeds.recordings.recordings_create.urls',
        namespace='create')),
)
