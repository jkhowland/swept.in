from django.contrib import admin
from settings.models import Setting, SettingType

class SettingAdmin(admin.ModelAdmin):
    list_display = ('user','setting_type',)

class SettingTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    
admin.site.register(Setting, SettingAdmin)
admin.site.register(SettingType, SettingTypeAdmin)