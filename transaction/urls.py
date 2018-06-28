from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views as core_views
from django.contrib.auth import views as auth_views
from . views import *


urlpatterns = [
	url(r'^$', home, name='index'),
	url(r'^profile/$', profile, name='profile'),
	url(r'^transaction/$', transaction, name='transaction'),
	url(r'^about/$', about, name='about'),
	url(r'^contact/$', contact, name='contact'),
	url(r'^services/$', services, name='services'),

	# url(r'^/$', Home.as_view(), name='home'),
	url(r'^login/$', auth_views.login, name='login'),
		# to specify wer login file is apart from registration/login
	# url(r'^login/$', auth_views.login, {'template_name': 'mysite/login_user.html'})
	url(r'^logout/$', auth_views.logout, name='logout'),
	# url(r'^$', home),
 	#url(r'^register/', register),


  	url(r'^signup/$', core_views.signup, name='signup'),
	
  	url(r'^createrecord/$', record, name='createrecord'),
	url(r'^recorddelete/(?P<id>\d+)/$', recorddelete,  name="recorddelete"),
	url(r'^recordview/(?P<id>\d+)/$', recordview ,name="recordview" ),
	url(r'^recordedit/(?P<id>\d+)/$', recordedit ,name="recordedit" ),
]