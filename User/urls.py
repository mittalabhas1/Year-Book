from django.conf.urls import patterns, url

from User import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^login/$', views.login, name='login'),
    url(r'^(?P<username>\d+)/$', views.HomeView.as_view(), name='home'),
)