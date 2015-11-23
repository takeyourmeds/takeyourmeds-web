from django.conf.urls import url

from . import views

urlpatterns = (
    url(r'^recordings$', views.view,
        name='view'),
)