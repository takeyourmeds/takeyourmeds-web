from django.conf.urls import url, patterns

urlpatterns = patterns('takeyourmeds.telephony.views',
    url(r'^telephony/info/(?P<ident>\w{40})$', 'callback',
        name='callback'),
)
