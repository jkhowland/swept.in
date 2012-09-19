from models import UserProfile
from django.contrib import admin

class UserProfileAdmin(admin.ModelAdmin):
  list_display = ('user',)
  list_display_links = ('user',)

admin.site.register(UserProfile, UserProfileAdmin)