from django.conf.urls.defaults import patterns, url
from django.contrib.auth import views as auth_views
from django.views.generic.simple import direct_to_template

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^signup/$', 'signup.views.signup'),
    url(r'^signup/submit/$', 'signup.views.earlyAccessSubmit'),
    url(r'^signup/send/$', 'signup.views.getInTouchSend'),
    url(r'^signup/thanks/$', 'signup.views.thanks'),                       
)
