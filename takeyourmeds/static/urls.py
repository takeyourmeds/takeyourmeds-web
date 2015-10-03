from django.conf.urls import patterns, url
from django.views.generic import TemplateView

urlpatterns = patterns('takeyourmeds.static.views',
    url('^$', TemplateView.as_view(template_name='static/index.html'),
        name='index'),
    url('^about$', TemplateView.as_view(template_name='static/about.html'),
        name='about'),
    url('^terms-and-conditions$', TemplateView.as_view(template_name='static/terms-and-conditions.html'),
        name='terms-and-conditions'),
    url('^privacy-policy$', TemplateView.as_view(template_name='static/privacy-policy.html'),
        name='privacy-policy'),
)
