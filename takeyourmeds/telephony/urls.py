from django.conf.urls import url

from . import views

urlpatterns = (
    url(r'^telephony/info/(?P<ident>\w{40})$', views.callback,
        name='callback'),
)
