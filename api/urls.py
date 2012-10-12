from django.conf.urls.defaults import patterns, url, include
from tastypie.api import Api
from api.resources import AccountsResource, UserResource, SettingTypeResource, SettingResource, SubUserResource, SubUserDataResource, ActivityGroupResource, ActivityResource, EventResource, AchievementTypeResource, AchievementResource

v1_api = Api(api_name='v1')
v1_api.register(AccountsResource())
v1_api.register(UserResource())
v1_api.register(SettingTypeResource())
v1_api.register(SettingResource())
v1_api.register(SubUserResource())
v1_api.register(SubUserDataResource())
v1_api.register(AchievementTypeResource())
v1_api.register(AchievementResource())
v1_api.register(ActivityGroupResource())
v1_api.register(ActivityResource())
v1_api.register(EventResource())


urlpatterns = patterns('',
  url(r'^', include(v1_api.urls)),
)
