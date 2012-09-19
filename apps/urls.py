from django.conf.urls.defaults import patterns, url, include
from django.contrib.auth import views as auth_views
from django.views.generic.simple import direct_to_template


from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
  url(r'^(?P<app_slug>[a-z-0-9]+),(?P<app_id>[0-9]+)/settings/', include('settings.urls')),
  
)
