from django.conf.urls import patterns, url

urlpatterns = patterns('takeyourmeds.registration.views',
    url(r'^register$', 'view',
        name='view'),
)
