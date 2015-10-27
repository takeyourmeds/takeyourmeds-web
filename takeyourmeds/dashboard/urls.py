from django.conf.urls import patterns, url

urlpatterns = patterns('takeyourmeds.dashboard.views',
    url(r'^dashboard$', 'view',
        name='view'),
)