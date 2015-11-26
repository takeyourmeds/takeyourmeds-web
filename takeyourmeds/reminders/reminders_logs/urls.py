from django.conf.urls import url

from . import views

urlpatterns = (
    url(r'^reminders/logs/(?P<slug>\w+)$', views.view,
        name='view'),
)
