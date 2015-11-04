from django.conf.urls import url

from . import views

urlpatterns = (
    url('^$', views.landing,
        name='landing'),

    url('^about$', views.about,
        name='about'),
    url('^faq$', views.faq,
        name='faq'),
    url('^contact$', views.contact,
        name='contact'),

    url('^terms-and-conditions$', views.terms,
        name='terms'),
    url('^privacy-policy$', views.privacy,
        name='privacy'),

    url('^404$', views.http404,
        name='http-404'),
    url('^500$', views.http500,
        name='http-500'),
    url('^admin$', views.admin,
        name='admin'),
)
