from django.conf.urls.defaults import patterns, url
from django.contrib.auth import views as auth_views
from django.views.generic.simple import direct_to_template
from registration.views import activate
from registration.views import register
from emailusernames.forms import EmailAuthenticationForm
from forms import NewsletterEmailUserCreationForm, ForgivingEmailAuthenticationForm, BetterPasswordResetForm

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
  url(r'^about/$', direct_to_template, {'template': 'registration/about.html'}),
  url(r'^login/$', 'django.contrib.auth.views.login', {'authentication_form': ForgivingEmailAuthenticationForm}, name='auth_login'),
  url(r'^logout/$', auth_views.logout, {'template_name': 'registration/logout.html', 'next_page': '/'}, name='auth_logout'),
  url(r'^password/change/$', auth_views.password_change, name='auth_password_change'),
  url(r'^password/change/done/$', auth_views.password_change_done, name='auth_password_change_done'),
  url(r'^password/reset/$', auth_views.password_reset, {'password_reset_form': BetterPasswordResetForm}, name='auth_password_reset'),
  url(r'^password/reset/confirm/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', auth_views.password_reset_confirm, name='auth_password_reset_confirm'),
  url(r'^password/reset/complete/$', auth_views.password_reset_complete, name='auth_password_reset_complete'),
  url(r'^password/reset/done/$', auth_views.password_reset_done, name='auth_password_reset_done'),
  url(r'^activate/complete/$', direct_to_template, {'template': 'registration/activation_complete.html'}, name='registration_activation_complete'),
  # Activation keys get matched by \w+ instead of the more specific
  # [a-fA-F0-9]{40} because a bad activation key should still get to the view;
  # that way it can return a sensible "invalid key" message instead of a
  # confusing 404.
  url(r'^activate/(?P<activation_key>\w+)/$', activate, {'backend': 'accounts.backends.NewsletterBackend'}, name='registration_activate'),
  url(r'^register/$', register, {'backend': 'accounts.backends.NewsletterBackend', 'form_class': NewsletterEmailUserCreationForm}, name='registration_register'),
  url(r'^register/complete/$', direct_to_template, {'template': 'registration/registration_complete.html'}, name='registration_complete'),
  url(r'^register/closed/$', direct_to_template, {'template': 'registration/registration_closed.html'}, name='registration_disallowed'),
  url(r'^profile/$', 'accounts.views.profile'),
  url(r'^newsletter-preferences/$', 'accounts.views.newsletter_preferences', name='newsletter_preferences'),
  url(r'^mailchimp-webhook/$', 'accounts.views.mailchimp_webhook'),
)
