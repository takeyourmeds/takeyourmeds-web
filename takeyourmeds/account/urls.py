from django.conf.urls import url, include

from . import views

urlpatterns = (
    url(r'', include('takeyourmeds.account.forgot_password.urls',
        namespace='forgot-password')),

    url(r'^login$', views.login,
        name='login'),
    url(r'^logout$', views.logout,
        name='logout'),
)
