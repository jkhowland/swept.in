
from django.db import models
from django.contrib.auth.models import User
from subusers.models import SubUser

class ActivityGroup(models.Model):
  subuser = models.ForeignKey(SubUser)
  name = models.CharField(max_length=200)
  description = models.TextField()

class Activity(models.Model):
  kit_id = models.CharField(max_length=200)
  subuser = models.ForeignKey(SubUser)
  name = models.CharField(max_length=200)
  description = models.TextField()
  user_json = models.TextField()
  
  def __unicode__(self):
    return self.name
  
class Event(models.Model):
  task_id = models.CharField(max_length=200)
  activity = models.ForeignKey(Activity)
  starting_time = models.DateTimeField()
  ending_time = models.DateTimeField()
  description = models.TextField()
  notes = models.TextField()

  def __unicode__(self):
    return self.description

class AchievementType(models.Model):
  name = models.CharField(max_length=200)
  description = models.TextField()
  achievement_min = models.IntegerField()
  achievement_max = models.IntegerField()

  def __unicode__(self):
    return self.name


class Achievement(models.Model):
  subuser = models.ForeignKey(SubUser)
  achievement_type = models.ForeignKey(AchievementType)
  percentage = models.DecimalField(max_digits=1, decimal_places=1)
  timestamp = models.DateTimeField()
  value = models.TextField()
  
  def __unicode__(self):
    return self.subuser + ' - ' + self.timestamp