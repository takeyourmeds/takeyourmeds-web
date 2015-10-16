from django.conf.urls import patterns, url

urlpatterns = patterns('takeyourmeds.static.views',
    url('^$', 'landing',
        name='landing'),

    url('^about$', 'about',
        name='about'),
    url('^faq$', 'faq',
        name='faq'),
    url('^contact$', 'contact',
        name='contact'),

    url('^terms-and-conditions$', 'terms',
        name='terms'),
    url('^privacy-policy$', 'privacy',
        name='privacy'),

    url('^admin$', 'admin',
        name='admin'),
)
