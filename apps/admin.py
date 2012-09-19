from django.contrib import admin
from apps.models import App

class AppAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {'slug':('name',)}
    

admin.site.register(App, AppAdmin)