from django.conf.urls import patterns, url

urlpatterns = patterns('takeyourmeds.groups.groups_admin.views',
    url(r'^admin/groups$', 'index',
        name='index'),
    url(r'^admin/groups/(?P<group_id>\d+)$', 'view',
        name='view'),
)
