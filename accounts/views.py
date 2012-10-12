from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from forms import NewsletterPreferencesForm
from django.utils import simplejson
from django.contrib.auth.models import User
from mailsnake import MailSnake
from django.conf import settings
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)

@login_required
def profile(request):
  return render(request, 'profile.html')

@login_required
def newsletter_preferences(request):
  profile = request.user.get_profile()
  
  if request.method == 'POST':
    form = NewsletterPreferencesForm(request.POST)
    
    if form.is_valid():
      profile.newsletter = form.cleaned_data['newsletter']
      profile.save()

      return redirect('/profile/')
    
  else:
    form = NewsletterPreferencesForm(initial={'newsletter': 'True' if profile.newsletter else 'False'})
  
  return render(request, 'newsletter_preferences.html', { 'form': form, })

def mailchimp_webhook(request):
  '''
  This view is called via a MailChimp webhook.
  '''
  response = {}
  
  try:
    if request.GET['secret'] == 'WZnI3VUbvQxe4hjcRj8i5tEXpTyk7XMHgdRiu12SUVE':
      webhook_type = request.POST['type']
      
      if webhook_type == 'subscribe':
        email = request.POST['data[email]']
 
        # Update the user's preference if the user exists
        try:
          user = User.objects.get(email=email)
        except User.DoesNotExist:
          pass
        else:
          profile = user.get_profile()
          if profile:
            profile.newsletter = True
            profile.save(dispatch_signal=False)
            
      elif webhook_type == 'unsubscribe' or webhook_type == 'cleaned':
        email = request.POST['data[email]']
  
        # Update the user's preference if the user exists
        try:
          user = User.objects.get(email=email)
        except User.DoesNotExist:
          pass
        else:
          profile = user.get_profile()
          if profile:
            profile.newsletter = False
            profile.save(dispatch_signal=False)
            
      elif webhook_type == 'upemail':
        old_email = request.POST['data[old_email]']
        new_email = request.POST['data[new_email]']
        
        mailsnake = MailSnake(settings.MAILCHIMP_API_KEY)
        
        # Update the user's preference if the user exists
        try:
          user = User.objects.get(email=old_email)
        except User.DoesNotExist:
          pass
        else:
          profile = user.get_profile()
          if profile:
            try:
              info = mailsnake.listMemberInfo(id=settings.MAILCHIMP_LIST_ID, email_address=(old_email,))
            except:
              logger.exception('Failed to retrieve subscription info for ' + old_email + ' from MailChimp')
            else:
              if info['success'] == 1 and info['data'][0]['status'] == 'subscribed':          
                profile.newsletter = True
              else:          
                profile.newsletter = False
              profile.save(dispatch_signal=False)
        
        # Update the user's preference if the user exists
        try:
          user = User.objects.get(email=new_email)
        except User.DoesNotExist:
          pass
        else:
          profile = user.get_profile()
          if profile:
            try:
              info = mailsnake.listMemberInfo(id=settings.MAILCHIMP_LIST_ID, email_address=(new_email,))
            except:
              logger.exception('Failed to retrieve subscription info for ' + new_email + ' from MailChimp')
            else:
              if info['success'] == 1 and info['data'][0]['status'] == 'subscribed':          
                profile.newsletter = True
              else:          
                profile.newsletter = False
              profile.save(dispatch_signal=False)
      
      response['success'] = 1
    else:
      response['success'] = 0
  except:
    response['success'] = 0
    
  return HttpResponse(simplejson.dumps(response), mimetype='application/json')
