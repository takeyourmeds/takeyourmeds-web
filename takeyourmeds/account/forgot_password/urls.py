from django.conf.urls import url

from . import views

urlpatterns = (
    url(r'^account/forgot-password$', views.view,
        name='view'),
    url(r'^account/forgot-password/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)$', views.reset,
        name='reset'),
)
