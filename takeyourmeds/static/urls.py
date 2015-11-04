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

    url('^404$', 'http404',
        name='http-404'),
    url('^500$', 'http500',
        name='http-500'),
    url('^admin$', 'admin',
        name='admin'),
)
