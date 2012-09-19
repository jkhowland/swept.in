from django.conf.urls.defaults import patterns, url
from django.contrib.auth import views as auth_views
from django.views.generic.simple import direct_to_template

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
  url(r'^$', 'settings.views.index'),
  url(r'^add-setting$', 'settings.views.add_setting')
)
