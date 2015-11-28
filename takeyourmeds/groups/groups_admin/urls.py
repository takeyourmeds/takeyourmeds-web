from django.conf.urls import url

from . import views

urlpatterns = (
    url(r'^admin/groups$', views.index,
        name='index'),
    url(r'^admin/groups/(?P<group_id>\d+)$', views.view,
        name='view'),
    url(r'^admin/groups/(?P<group_id>\d+)/create-access-tokens$', views.create_access_tokens,
        name='create-access-tokens'),
)
