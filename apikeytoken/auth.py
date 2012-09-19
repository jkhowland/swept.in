from tastypie.authentication import Authentication
from tastypie.authorization import Authorization
from tastypie.http import HttpUnauthorized
from models import ApiKey, ApiKeyToken
from registration.models import RegistrationProfile
import logging

logger = logging.getLogger(__name__)

class ApiKeyTokenAuthentication(Authentication):
  """
  Handles API key/token auth, in which a user provides an API key and usually a token.
  
  Set require_user to require that authorization include a valid token. This should be
  the case for most API. Exceptions include account registration and session initiation.
  
  Set require_active to require that the user be active (except when the user is pending activation).
  This allows users to be deactivated, preventing API access, without deleting them.
  
  Set require_activated to required that the user be activated (regardless of whether the user is active).
  By default activation is not required, allowing API access before a user has completed registration.
  """
  def __init__(self, require_user=True, require_active=True, require_activated=False):
    self.require_user = require_user
    self.require_active = require_active
    self.require_activated = require_activated
  
  def _unauthorized(self):
    return HttpUnauthorized()

  def is_authenticated(self, request, **kwargs):
    """
    Authenticates the API key and, if provided, user token
    """
    if request.META.get('HTTP_AUTHORIZATION') and request.META['HTTP_AUTHORIZATION'].lower().startswith('apikey '):
      data = request.META['HTTP_AUTHORIZATION'].split()[1:][0]
      (key, token) = data.split(':', 1) if ':' in data else (data, None)

      # Validate the API key
      try:
        request.api_key = ApiKey.objects.get(value=key, is_active=True)
      except ApiKey.DoesNotExist:
        logger.error('API key ' + key + ' does not exist or is inactive')
        return self._unauthorized()
      
      if token is not None:        
        # Validate the token and get the corresponding user
        try:
          request.token = ApiKeyToken.objects.get(value=token, api_key=request.api_key)
          request.user = request.token.user
        except ApiKeyToken.DoesNotExist:
          logger.error('Token ' + token + ' does not exist for API key ' + request.api_key.value)
          return self._unauthorized()
        
      if self.require_user:
        if not hasattr(request, 'user') or request.user is None or not request.user.is_authenticated():
          logger.error('User is not authenticated')
          return self._unauthorized()
        
        if self.require_active or self.require_activated:
          try:
            profile = RegistrationProfile.objects.get(user=request.user)
          except RegistrationProfile.DoesNotExist:
            profile = None
          
          if self.require_active and not request.user.is_active and profile is None:
            logger.error('Request requires an active user, but user is inactive and is not pending activation')
            return self._unauthorized()
          
          if self.require_activated and not request.user.is_active and (profile is not None or profile.activation_key == profile.ACTIVATED):
            logger.error('Request requires an activated user, but user is pending activation')
            return self._unauthorized()

      return True

    logger.error('Missing apikey Authorization header')
    return self._unauthorized()

  def get_identifier(self, request):
    """
    Provides a unique string identifier for the requestor.
    """
    if hasattr(request, 'user') and hasattr(request.user, 'email'):
      return request.user.email

    return 'nouser'
