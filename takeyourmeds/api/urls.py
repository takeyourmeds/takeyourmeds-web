from django.conf.urls import url, patterns

urlpatterns = patterns('takeyourmeds.api.views',
    url(r'^trigger/$', 'trigger_now',
        name='trigger_now'),
)
