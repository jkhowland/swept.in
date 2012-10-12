from django.contrib import admin
from events.models import ActivityGroup, Activity, Event, AchievementType, Achievement

class ActivityGroupAdmin(admin.ModelAdmin):
  list_display = ('name',)

class ActivityAdmin(admin.ModelAdmin):
  list_display = ('name','subuser',) 

class EventAdmin(admin.ModelAdmin):
  list_display = ('description',)
  
class AchievementTypeAdmin(admin.ModelAdmin):
  list_display = ('name',)

class AchievementAdmin(admin.ModelAdmin):
  list_display = ('subuser', 'percentage')

admin.site.register(ActivityGroup, ActivityGroupAdmin)
admin.site.register(Activity, ActivityAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(AchievementType, AchievementTypeAdmin)
admin.site.register(Achievement, AchievementAdmin)