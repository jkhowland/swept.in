from django.contrib import admin
from subusers.models import SubUser, SubUserData

class SubUserAdmin(admin.ModelAdmin):
    list_display = ('user','name',)

class SubUserDataAdmin(admin.ModelAdmin):
    list_display = ('subuser','app','value',)

    
admin.site.register(SubUser, SubUserAdmin)
admin.site.register(SubUserData, SubUserDataAdmin)
