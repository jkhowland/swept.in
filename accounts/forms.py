from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import PasswordResetForm
from emailusernames.forms import EmailUserCreationForm, EmailAuthenticationForm
from django.utils.translation import ugettext_lazy as _

ERROR_MESSAGE = _("Your username and password didn't match. Please try again.")
ERROR_MESSAGE_INACTIVE = _("This account has not yet been confirmed. Please check your email and click on the link to finish creating your account.")

BOOLEAN_CHOICES = ((True, 'Yes'), (False, 'No'))

class ForgivingEmailAuthenticationForm(EmailAuthenticationForm):
  message_incorrect_password = ERROR_MESSAGE
  message_inactive = ERROR_MESSAGE_INACTIVE

  def clean(self):
    email = self.cleaned_data.get('email')
    password = self.cleaned_data.get('password')

    if email and password:
      self.user_cache = authenticate(email=email, password=password)
      if (self.user_cache is None):
        raise forms.ValidationError(self.message_incorrect_password)
      if not self.user_cache.is_active:
        raise forms.ValidationError(self.message_inactive)
    self.check_for_test_cookie()
    return self.cleaned_data
  
def boolean_coerce(value):
  # value is received as a unicode string
  if str(value).lower() in ('1', 'true'):
    return True
  elif str(value).lower() in ('0', 'false'):
    return False
  return None

class NewsletterEmailUserCreationForm(EmailUserCreationForm):
  newsletter = forms.TypedChoiceField(coerce=boolean_coerce, choices=BOOLEAN_CHOICES, widget=forms.RadioSelect, required=True)
  
  def clean(self):
    cleaned_data = super(NewsletterEmailUserCreationForm, self).clean()
    if cleaned_data.has_key('email'):
      cleaned_data['username'] = cleaned_data['email']
    return cleaned_data
  
class BetterPasswordResetForm(PasswordResetForm):
  def __init__(self, *args, **kwargs):
    super(BetterPasswordResetForm, self).__init__(*args, **kwargs)
    self.fields['email'].label = 'Email'
  
class NewsletterPreferencesForm(forms.Form):
  newsletter = forms.TypedChoiceField(coerce=boolean_coerce, choices=BOOLEAN_CHOICES, widget=forms.RadioSelect, required=True)