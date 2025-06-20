# Models for octofit_tracker
from django.db import models
from djongo import models as djongo_models

# Add your models here
class User(models.Model):
    _id = djongo_models.ObjectIdField()
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

class Team(models.Model):
    _id = djongo_models.ObjectIdField()
    name = models.CharField(max_length=100, unique=True)
    members = djongo_models.ArrayReferenceField(to=User, on_delete=models.CASCADE)

class Activity(models.Model):
    _id = djongo_models.ObjectIdField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=100)
    duration = models.DurationField()

class Leaderboard(models.Model):
    _id = djongo_models.ObjectIdField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField()

class Workout(models.Model):
    _id = djongo_models.ObjectIdField()
    name = models.CharField(max_length=100)
    description = models.TextField()
