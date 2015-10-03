from django.conf.urls import url, patterns

urlpatterns = patterns('takeyourmeds.telephony.views',
    url('^telephony/info/(?P<uuid>.*)$', 'info',
        name='info'),
)
