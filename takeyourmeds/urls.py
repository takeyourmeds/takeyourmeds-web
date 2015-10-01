from rest_framework import routers

from django.conf.urls import include, url
from django.views.generic import TemplateView

from reminder.api import ReminderViewSet

router = routers.DefaultRouter()
router.register(r'reminders', ReminderViewSet)

urlpatterns = [
    url('^$', TemplateView.as_view(template_name='index.html')),
    url('^about$', TemplateView.as_view(template_name='about.html')),
    url('^terms-and-conditions$', TemplateView.as_view(template_name='terms-and-conditions.html')),
    url('^privacy-policy$', TemplateView.as_view(template_name='privacy-policy.html')),
    url('^telephony/', include("takeyourmeds.telephony.urls")),
    url('^reminder/', include("takeyourmeds.reminder.urls")),
    url(r'^api/', include(router.urls)),
    url(r'^accounts/', include('allauth.urls')),
]
