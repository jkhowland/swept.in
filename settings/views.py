from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect
from settings.models import SettingType, Setting

@login_required
def index(request,app_slug,app_id):
  return render(request, 'index.html', {})


@login_required
def add_setting(request):
  setting_type = get_object_or_404(SettingType, pk=request.GET['type'])
  setting = Setting()
  setting.setting_type = setting_type
  setting.user = request.user
  setting.value = request.GET['value']
  setting.save()
  return redirect('.')