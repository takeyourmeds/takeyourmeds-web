from django.conf.urls import url, patterns

urlpatterns = patterns('takeyourmeds.telephony.views',
    url('^info/(?P<uuid>.*)$', 'info',
        name='info'),
)
