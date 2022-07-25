import datetime
from time import time

from django.db import models
from django.utils import timezone
from django.contrib import admin
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Log1(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="log1", null=True) #when profile is deleted, user is not but not vice vers
    time1 = models.CharField(max_length=50)
    time2 = models.CharField(max_length=50)
    time3 = models.CharField(max_length=50)
    time4 = models.CharField(max_length=50)
    time5 = models.CharField(max_length=50)
    time6 = models.CharField(max_length=50)
    pub_date = models.DateField(auto_now_add=True)
    # pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "6x400m -" + str(self.pub_date)

class Log2(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="log2", null=True) #when profile is deleted, user is not but not vice vers
    time1 = models.CharField(max_length=50)
    time2 = models.CharField(max_length=50)
    time3 = models.CharField(max_length=50)
    pub_date = models.DateTimeField(auto_now_add=True)

    @admin.display(
        boolean=True,
        ordering='pub_date',
        description='Published recently?',
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    def __str__(self):
        return "3x800m -" + str(self.pub_date)

class Goal(models.Model):
    Goal_choices = [
    ('8', '8 mins'),
    ('9', '9 mins'),
    ('10', '10 mins'),
    ('11', '11 mins'),
    ('12', '12 mins'),
    ('13', '13 mins'),
    ('14', '14 mins'),
    ('15', '15 mins'),
    ('16', '16 mins'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile", null=True)
    goal_time = models.CharField(
        max_length = 20,
        choices = Goal_choices,
        default = '12'
        )
    goal_date = models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.user.username + "Profile"

    # def save(self):
    #     super().save()
    #     weeks_to_goal = (self.goal_date - datetime.now()) / 7

