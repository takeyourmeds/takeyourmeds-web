"""nhs_reminder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView

from reminder.views import send, sent

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url('^$', TemplateView.as_view(template_name='index.html')),
    url('^about$', TemplateView.as_view(template_name='about.html')),
    url('^send/$', send, name='send'),
    url('^sent/$', sent, name='sent'),
    url('^telephony/', include("telephony.urls")),
    url('^reminder/', include("reminder.urls")),
    url(r'^api/', include('reminder.urls')),
    url(r'^accounts/', include('allauth.urls')),
]
