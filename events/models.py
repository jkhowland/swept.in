
from django.db import models
from django.contrib.auth.models import User
from apps.models import App
from subusers.models import SubUser

class ActivityGroup(models.Model):
  subuser = models.ForeignKey(SubUser)
  name = models.CharField(max_length=200)
  description = models.TextField()

class Activity(models.Model):
  subuser = models.ForeignKey(SubUser)
  app = models.ForeignKey(App)
  activity_group = models.ForeignKey(ActivityGroup, blank=True, null=True)
  name = models.CharField(max_length=200)
  description = models.TextField()
  subject = models.CharField(max_length=200)
  curriculum_bool = models.IntegerField()
  
  def __unicode__(self):
    return self.name
  
class Event(models.Model):
  activity = models.ForeignKey(Activity)
  starting_time = models.DateTimeField()
  ending_time = models.DateTimeField()

  ANSWER_TYPE_CHOICES = (
    ('M', 'Multiple Choice'),
    ('F', 'Fill In The Blank'),
    ('P', 'Puzzle'),
                         )
  answer_type = models.CharField(max_length=1, choices=ANSWER_TYPE_CHOICES)
  question_description = models.TextField()
  answer_array = models.TextField()
  percentage = models.DecimalField(max_digits=1, decimal_places=1)

  def __unicode__(self):
    return self.question_description

class AchievementType(models.Model):
  app = models.ForeignKey(App)
  name = models.CharField(max_length=200)
  description = models.TextField()
  curriculum_bool = models.IntegerField()
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
    return self.value