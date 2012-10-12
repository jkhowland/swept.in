from django.db import models
from django.contrib.auth.models import User
    
class SettingType(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    
    SETTINGS_TYPE_CHOICES = ( 
      ('I', 'Integer'), 
      ('S', 'String'),
      ('A', 'Array' ),
      ('B', 'Boolean'),
      ('D', 'Date'),
      ) 
    
    type = models.CharField(max_length=1, choices=SETTINGS_TYPE_CHOICES)
    setting_max = models.IntegerField()
    setting_min = models.IntegerField()
        
    value_max = models.IntegerField()
    value_min = models.IntegerField()    
        
    def __unicode__(self):
        return self.name

    
class Setting(models.Model):
    user = models.ForeignKey(User)
    setting_type = models.ForeignKey(SettingType)
    value = models.TextField()