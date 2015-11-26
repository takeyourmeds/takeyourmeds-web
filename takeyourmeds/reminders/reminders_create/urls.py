from django.conf.urls import url

from . import views

urlpatterns = (
    url(r'^reminders/create$', views.view,
        name='view'),
)
