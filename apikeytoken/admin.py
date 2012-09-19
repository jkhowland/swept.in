from models import ApiKey, ApiKeyToken
from django.contrib import admin

class ApiKeyAdmin(admin.ModelAdmin):
  list_display = ('value', 'is_active', 'date_created',)
  list_display_links = ('value',)

class ApiKeyTokenAdmin(admin.ModelAdmin):
  list_display = ('value', 'user', 'date_created',)
  list_display_links = ('value',)

admin.site.register(ApiKey, ApiKeyAdmin)
admin.site.register(ApiKeyToken, ApiKeyTokenAdmin)