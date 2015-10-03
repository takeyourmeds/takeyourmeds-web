from django.conf.urls import patterns, url

urlpatterns = patterns('takeyourmeds.static.views',
    url('^$', 'index',
        name='index'),
    url('^about$', 'about',
        name='about'),
    url('^terms-and-conditions$', 'terms_and_conditions',
        name='terms-and-conditions'),
    url('^privacy-policy$', 'privacy_policy',
        name='privacy-policy'),
)
