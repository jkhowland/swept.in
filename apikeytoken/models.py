from django.db import models
from django.contrib.auth.models import User

class ApiKey(models.Model):
  value = models.CharField(max_length=40, unique=True)
  is_active = models.BooleanField()
  date_created = models.DateTimeField(auto_now_add=True)
  
class ApiKeyToken(models.Model):
  api_key = models.ForeignKey(ApiKey)
  user = models.ForeignKey(User)
  value = models.CharField(max_length=40, unique=True)
  date_created = models.DateTimeField(auto_now_add=True)