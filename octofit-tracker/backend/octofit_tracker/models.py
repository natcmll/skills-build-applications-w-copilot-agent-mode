from djongo import models
from bson import ObjectId

class User(models.Model):
    id = models.ObjectIdField(primary_key=True, default=ObjectId, editable=False)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

class Team(models.Model):
    id = models.ObjectIdField(primary_key=True, default=ObjectId, editable=False)
    name = models.CharField(max_length=255)
    members = models.JSONField()

class Activity(models.Model):
    id = models.ObjectIdField(primary_key=True, default=ObjectId, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=255)
    duration = models.IntegerField()

class Leaderboard(models.Model):
    id = models.ObjectIdField(primary_key=True, default=ObjectId, editable=False)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    score = models.IntegerField()

class Workout(models.Model):
    id = models.ObjectIdField(primary_key=True, default=ObjectId, editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField()
