from django.contrib.auth.models import User
from tastypie.resources import Resource, ModelResource
from tastypie.authentication import Authentication
from django.db import IntegrityError
from tastypie.resources import fields
from tastypie.exceptions import BadRequest, ImmediateHttpResponse
from apikeytoken.auth import ApiKeyTokenAuthentication
from tastypie.authorization import Authorization
from accounts.backends import NewsletterBackend
from django.core.validators import validate_email
from django.contrib.auth import authenticate
import random
import time
import hashlib
from apikeytoken.models import ApiKey, ApiKeyToken
from django.conf.urls.defaults import url
from tastypie import http
from django.http import HttpResponse
from registration.models import RegistrationProfile
from serializers import CustomJSONSerializer
import logging
from settings.models import SettingType, Setting
from subusers.models import SubUser, SubUserData
from events.models import ActivityGroup, Activity, Event, AchievementType, Achievement

logger = logging.getLogger(__name__)

class AccountsResource(Resource):
  class Meta:
    resource_name = 'accounts'
    list_allowed_methods = []
    detail_allowed_methods = []
    authentication = ApiKeyTokenAuthentication()
    authorization = Authorization()
    serializer = CustomJSONSerializer(formats=['json'])
    
  def override_urls(self):
    return [
      url(r"^(?P<resource_name>%s)/register/$" % (self._meta.resource_name), self.wrap_view('register'), name="api_accounts_register"),
      url(r"^(?P<resource_name>%s)/generate-token/$" % (self._meta.resource_name), self.wrap_view('generate_token'), name="api_accounts_generate_token"),
      url(r"^(?P<resource_name>%s)/expire-token/$" % (self._meta.resource_name), self.wrap_view('expire_token'), name="api_accounts_expire_token"),
    ]
    
  def register(self, request, **kwargs):    
    self.method_check(request, allowed=['post'])
    self.is_authenticated_apikey_only(request)
    self.is_authorized(request)
    self.throttle_check(request)
    
    deserialized = self.deserialize(request, request.raw_post_data, format=request.META.get('CONTENT_TYPE', 'application/json'))
    deserialized = self.alter_deserialized_detail_data(request, deserialized)
    
    email = deserialized['email'] or ''
    password = deserialized['password'] or ''
    newsletter = bool(deserialized['newsletter'])
    
    try:
      validate_email(email)
    except:
      raise BadRequest('Please provide a valid email address.')
    
    if password == '':
      raise BadRequest('Please provide a password.')
    
    try:
      NewsletterBackend().register(request, username=email, email=email, password1=password, newsletter=newsletter)
    except IntegrityError:
      raise BadRequest('A user with that email address already exists.')
    
    self.log_throttled_access(request)
    return http.HttpAccepted()
    
  def generate_token(self, request, **kwargs):
    self.method_check(request, allowed=['post'])
    self.is_authenticated_apikey_only(request)
    self.is_authorized(request)
    self.throttle_check(request)
    
    deserialized = self.deserialize(request, request.raw_post_data, format=request.META.get('CONTENT_TYPE', 'application/json'))
    deserialized = self.alter_deserialized_detail_data(request, deserialized)
    
    email = deserialized['email'] or ''
    password = deserialized['password'] or ''
    
    user = authenticate(email=email, password=password)
    if user is None:
      logger.error('Invalid email ' + email + ' and password combination')
      raise BadRequest('Failed to authenticate.')
    
    token = hashlib.sha1(str(random.random()) + '3bae59df117289af59' + str(time.time())).hexdigest()
    
    api_key_token = ApiKeyToken(value=token, api_key=request.api_key, user=user)
    api_key_token.save()
    
    self.log_throttled_access(request)
    return self.create_response(request, {'token': token}, response_class=http.HttpCreated)
  
  def expire_token(self, request, **kwargs):
    self.method_check(request, allowed=['post'])
    self.is_authenticated(request)
    self.is_authorized(request)
    self.throttle_check(request)

    if hasattr(request, 'token'):
      request.token.delete()
      
    self.log_throttled_access(request)
    return http.HttpAccepted()
  
  def is_authenticated_apikey_only(self, request):
    auth_result = ApiKeyTokenAuthentication(require_user=False).is_authenticated(request)

    if isinstance(auth_result, HttpResponse):
      raise ImmediateHttpResponse(response=auth_result)

    if not auth_result is True:
      raise ImmediateHttpResponse(response=http.HttpUnauthorized())


class UserResource(ModelResource):
  newsletter = fields.BooleanField()
  is_activated = fields.BooleanField()

  class Meta:
    queryset = User.objects.all()
    resource_name = 'users'
    fields = ['id', 'email', 'first_name', 'last_name', 'is_activated', 'newsletter']
    list_allowed_methods = ['get']
    detail_allowed_methods = ['get', 'put']
    authentication = ApiKeyTokenAuthentication()
    authorization = Authorization()
    serializer = CustomJSONSerializer(formats=['json'])
    
  def __init__(self, **kwargs):
    super(ModelResource, self).__init__(**kwargs)
    self.fields['id'].readonly = True
    self.fields['email'].readonly = True
    self.fields['is_activated'].readonly = True  
  
  def dehydrate_is_activated(self, bundle):
    if bundle.obj.is_active:
      return True
    
    try:
      RegistrationProfile.objects.get(user=bundle.obj)
    except RegistrationProfile.DoesNotExist:
      return True
    
    return False
    
  def dehydrate_newsletter(self, bundle):
    return bundle.obj.get_profile().newsletter
  
  def hydrate(self, bundle):
    profile = bundle.obj.get_profile()
    profile.newsletter = bundle.data['newsletter']
    profile.save()
    
    return bundle
  
  def apply_authorization_limits(self, request, object_list):
    '''
    Only permit access to the current user's user.
    '''
    return object_list.filter(id=request.user.id)
  
class SettingTypeResource(ModelResource):
  class Meta:
    queryset = SettingType.objects.all()
    resource_name = 'setting-types'
    list_allowed_methods = ['get']
    detail_allowed_methods = ['get']
    authentication = ApiKeyTokenAuthentication()
    authorization = Authorization()
    serializer = CustomJSONSerializer(formats=['json'])

  def get_object_list(self, request):
    return super(SettingTypeResource, self).get_object_list(request)


class SettingResource(ModelResource):
  setting_type = fields.ToOneField(SettingTypeResource, 'setting_type')
  
  class Meta:
    queryset = Setting.objects.all()
    resource_name = 'settings'
    list_allowed_methods = ['get','post']
    detail_allowed_methods = ['get','put','post','delete']
    authentication = ApiKeyTokenAuthentication()
    authorization = Authorization()
    serializer = CustomJSONSerializer(formats=['json'])

  def apply_authorization_limits(self, request, object_list):
    '''
    Only permit access to the current user's settings.
    '''
    return object_list.filter(user=request.user)

  def obj_create(self, bundle, request=None, **kwargs):
        return super(SettingResource, self).obj_create(bundle, request, user=request.user)

  def get_object_list(self, request):
    return super(SettingResource, self).get_object_list(request)

class SubUserResource(ModelResource):
  user = fields.ToOneField(UserResource, 'user')

  class Meta:
    queryset = SubUser.objects.all()
    resource_name = 'subusers'
    list_allowed_methods = ['get','post']
    detail_allowed_methods = ['get','put','post','delete']
    authentication = ApiKeyTokenAuthentication()
    authorization = Authorization()
    serializer = CustomJSONSerializer(formats=['json'])

  def apply_authorization_limits(self, request, object_list):
    '''
    Only permit access to the current user's subusers.
    '''
    return object_list.filter(user=request.user)

  def obj_create(self, bundle, request=None, **kwargs):
        return super(SubUserResource, self).obj_create(bundle, request, user=request.user)

  def get_object_list(self, request):
    return super(SubUserResource, self).get_object_list(request)
  

class SubUserDataResource(ModelResource): 
  subuser = fields.ToOneField(SubUserResource, 'subuser')
   
  class Meta:
    queryset = SubUserData.objects.all()
    resource_name = 'subuserdata'
    list_allowed_methods = ['get','post']
    detail_allowed_methods = ['get','put','post','delete']
    authentication = ApiKeyTokenAuthentication()
    authorization = Authorization()
    serializer = CustomJSONSerializer(formats=['json'])

  def apply_authorization_limits(self, request, object_list):
    '''
    Only permit access to the current user's subusers.
    '''
    return object_list.filter(subuser__user=request.user)

  def obj_create(self, bundle, request=None, **kwargs):
        return super(SubUserDataResource, self).obj_create(bundle, request)
        
  def get_object_list(self, request):
        return super(SubUserDataResource, self).get_object_list(request)

class ActivityGroupResource(ModelResource):
  subuser = fields.ToOneField(SubUserResource, 'subuser')
  
  class Meta:
    queryset = ActivityGroup.objects.all()
    resource_name = 'activity-groups'
    list_allowed_methods = ['get','post']
    detail_allowed_methods = ['get','put','post','delete']
    authentication = ApiKeyTokenAuthentication()
    authorization = Authorization()
    serializer = CustomJSONSerializer(formats=['json'])

  def apply_authorization_limits(self, request, object_list):
    '''
    Only permit access to the current user's settings.
    '''
    return object_list.filter(subuser__user=request.user)

  def obj_create(self, bundle, request=None, **kwargs):
        return super(AchievementResource, self).obj_create(bundle, request)

  def get_object_list(self, request):
    return super(AchievementResource, self).get_object_list(request).filter(subuser__user=request.user)



class ActivityResource(ModelResource):
  subuser = fields.ToOneField(SubUserResource, 'subuser')
  kit_id = fields.CharField(attribute='kit_id')

  class Meta:
    queryset = Activity.objects.all()
    resource_name = 'activities'
    list_allowed_methods = ['get','post']
    detail_allowed_methods = ['get','put','post','delete']
    authentication = ApiKeyTokenAuthentication()
    authorization = Authorization()
    serializer = CustomJSONSerializer(formats=['json'])

  def apply_authorization_limits(self, request, object_list):
    '''
    Only permit access to the current user's subusers.
    '''
    return object_list.filter(subuser__user=request.user)

  def obj_create(self, bundle, request=None, **kwargs):
    return super(ActivityResource, self).obj_create(bundle, request)

  def get_object_list(self, request):
    return super(ActivityResource, self).get_object_list(request)
  

class EventResource(ModelResource): 
  activity = fields.ToOneField(ActivityResource, 'activity')
  task_id = fields.CharField(attribute='task_id')
   
  class Meta:
    queryset = Event.objects.all()
    resource_name = 'events'
    list_allowed_methods = ['get','post']
    detail_allowed_methods = ['get','put','post','delete']
    authentication = ApiKeyTokenAuthentication()
    authorization = Authorization()
    serializer = CustomJSONSerializer(formats=['json'])

  def apply_authorization_limits(self, request, object_list):
    '''
    Only permit access to the current user's subusers.
    '''
    return object_list.filter(activity__subuser__user=request.user)

  def obj_create(self, bundle, request=None, **kwargs):
        return super(EventResource, self).obj_create(bundle, request)
        
  def get_object_list(self, request):
        return super(EventResource, self).get_object_list(request)


class AchievementTypeResource(ModelResource):
  class Meta:
    queryset = AchievementType.objects.all()
    resource_name = 'achievement-types'
    list_allowed_methods = ['get']
    detail_allowed_methods = ['get']
    authentication = ApiKeyTokenAuthentication()
    authorization = Authorization()
    serializer = CustomJSONSerializer(formats=['json'])

  def get_object_list(self, request):
    return super(AchievementTypeResource, self).get_object_list(request)


class AchievementResource(ModelResource):
  achievement_type = fields.ToOneField(AchievementTypeResource, 'achievement_type')
  subuser = fields.ToOneField(SubUserResource, 'subuser')
  
  class Meta:
    queryset = Achievement.objects.all()
    resource_name = 'achievements'
    list_allowed_methods = ['get','post']
    detail_allowed_methods = ['get','put','post','delete']
    authentication = ApiKeyTokenAuthentication()
    authorization = Authorization()
    serializer = CustomJSONSerializer(formats=['json'])

  def apply_authorization_limits(self, request, object_list):
    '''
    Only permit access to the current user's settings.
    '''
    return object_list.filter(subuser__user=request.user)

  def obj_create(self, bundle, request=None, **kwargs):
        return super(AchievementResource, self).obj_create(bundle, request)

  def get_object_list(self, request):
    return super(AchievementResource, self).get_object_list(request)
