from django import forms

class SignupForm(forms.Form):
  email = forms.EmailField()

class GetInTouchForm(forms.Form):
  name = forms.CharField(max_length = 100)
  sender = forms.EmailField()
  message = forms.CharField()