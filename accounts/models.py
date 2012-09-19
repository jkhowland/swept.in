from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.dispatch import receiver
from mailsnake import MailSnake
from django.conf import settings
import logging

logger = logging.getLogger(__name__)

class UserProfile(models.Model):
  user = models.OneToOneField(User)

  newsletter = models.BooleanField()
  
  def save(self, dispatch_signal=True, **kwargs):
    self.save_base(raw=not dispatch_signal, **kwargs)
  
@receiver(pre_save, sender=User, dispatch_uid="pre_save_user")
def pre_save_user(sender, instance, **kwargs):
  try:
    original = User.objects.get(pk=instance.pk)
  except User.DoesNotExist:
    pass
  else:
    # Sync with MailChimp whenever a user becomes active
    if not original.is_active == instance.is_active and instance.is_active:
      user = instance
      profile = user.get_profile()
      
      mailsnake = MailSnake(settings.MAILCHIMP_API_KEY)
  
      if profile.newsletter:
        email = user.email.encode('utf-8')
        
        logger.debug('Subscribing ' + email + ' to MailChimp list...')
        try:
          mailsnake.listSubscribe(id=settings.MAILCHIMP_LIST_ID, email_address=email, double_optin=False, update_existing=True, send_welcome=True)
        except:
          logger.exception('Failed to subscribe ' + email + ' to MailChimp list')
          
      else:
        email = user.email.encode('utf-8')
        
        # If the user is already subscribed on MailChimp, go ahead and update our local state to match
        logger.debug('Retrieving subscription state for ' + email + ' on MailChimp list...')
        try:
          info = mailsnake.listMemberInfo(id=settings.MAILCHIMP_LIST_ID, email_address=(email,))
        except:
          logger.exception('Failed to retrieve subscription state for ' + email)
        else:
          if info['success'] == 1 and info['data'][0]['status'] == 'subscribed':
            profile.newsletter = True
            profile.save(dispatch_signal=False)
  
@receiver(pre_save, sender=UserProfile, dispatch_uid="pre_save_user_profile")
def pre_save_user_profile(sender, instance, raw, **kwargs):
  # Don't update MailChimp if this is a raw save (to prevent cycles when updating in response to the MailChimp webhook)
  if not raw:
    try:
      original = UserProfile.objects.get(pk=instance.pk)
    except UserProfile.DoesNotExist:
      pass
    else:
      if not original.newsletter == instance.newsletter:
        user = instance.user
        # Update MailChimp whenever the newsletter preference changes for an active user
        if user.is_active:
          email = user.email.encode('utf-8')
          profile = instance
          
          mailsnake = MailSnake(settings.MAILCHIMP_API_KEY)
          
          if profile.newsletter:        
            logger.debug('Subscribing ' + email + ' to MailChimp list...')
            try:
              mailsnake.listSubscribe(id=settings.MAILCHIMP_LIST_ID, email_address=email, double_optin=False, update_existing=True, send_welcome=True)
            except:
              logger.exception('Failed to subscribe ' + email + ' to MailChimp list')
          else:
            logger.debug('Unsubscribing ' + email + ' from MailChimp list...')
            try:
              mailsnake.listUnsubscribe(id=settings.MAILCHIMP_LIST_ID, email_address=email)
            except:
              logger.exception('Failed to unsubscribe ' + email + ' from MailChimp list')
