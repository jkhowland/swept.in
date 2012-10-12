
from django.db import models
from django.contrib.auth.models import User


class SubUser(models.Model):
    user = models.ForeignKey(User)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    # profile picture, other information like birthday etc. to come
    
    def __unicode__(self):
      return self.name

    
class SubUserData(models.Model):
    subuser = models.ForeignKey(SubUser)
    value = models.TextField()
    
    def __unicode__(self):
      return self.value
