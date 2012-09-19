from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect
from apps.models import App
from settings.models import SettingType, Setting

@login_required
def index(request,app_slug,app_id):
  app = get_object_or_404(App, pk=app_id)
  available_setting_type_list = app.settingtype_set.all()
  settings_dictionary = {}
  
  for setting_type in available_setting_type_list:
    settings_dictionary[setting_type.id] = []
    
  user_defined_settings = request.user.setting_set.filter(setting_type__app=app)

  for setting in user_defined_settings:
    settings_dictionary[setting.setting_type.id].append(setting)
  
  return render(request, 'index.html', {'app':app,'available_setting_type_list':available_setting_type_list, 'settings_dictionary':settings_dictionary,})


@login_required
def add_setting(request,app_slug,app_id):
  app = get_object_or_404(App, pk=app_id)
  setting_type = get_object_or_404(SettingType, pk=request.GET['type'])
  setting = Setting()
  setting.app = app
  setting.setting_type = setting_type
  setting.user = request.user
  setting.value = request.GET['value']
  setting.save()
  return redirect('.')