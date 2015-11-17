from django.conf.urls import url

from . import views

urlpatterns = (
    url(r'^reminders/(?P<reminder_id>\d+)$', views.view,
        name='view'),
)
