from django.conf.urls import patterns, url

from User import views

urlpatterns = patterns('',
	url(r'^$', views.IndexView.as_view(), name='index'),
	url(r'^login/$', views.login, name='login'),
	url(r'^save/$', views.saveDetails, name='saveDetails'),
	url(r'^(?P<pk>\d+)/$', views.HomeView.as_view(), name='home'),
)