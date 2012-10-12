from django.conf.urls import patterns, include, url
from django.views.generic.simple import redirect_to
from django.views.generic.simple import direct_to_template

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
  url(r'^$', redirect_to, {'url': '/signup/'}),
  url(r'^', include('signup.urls')),
  url(r'^', include('accounts.urls')),
  url(r'^api/', include('api.urls')),
  url(r'^admin/', include(admin.site.urls)),
)

#  url(r'^$', redirect_to, {'url': '/profile/'}),
#  url(r'^', include('accounts.urls')),
