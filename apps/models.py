
from django.db import models
from apikeytoken.models import ApiKey

class App(models.Model):
    api_key = models.ForeignKey(ApiKey, blank=True, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField()
    slug = models.SlugField()    
    
    def __unicode__(self):
        return self.name

