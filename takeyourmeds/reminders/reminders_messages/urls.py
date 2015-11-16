from django.conf.urls import url

from . import views

urlpatterns = (
    url(r'^_/status-callback/messages/(?P<ident>.+)$', views.status_callback,
        name='status-callback'),
)
