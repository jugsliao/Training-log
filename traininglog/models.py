import datetime
from time import time

from django.db import models
from django.utils import timezone
from django.contrib import admin
from django.contrib.auth.models import User

# Create your models here.
class Log(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="log", null=True)
    title = models.CharField(max_length=50)
    description = models.TextField()
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
        return self.title + " - " + str(self.pub_date)

class Goal(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="goal", null=True)
    goal_description = models.CharField(max_length=50, default='Keep healthy')
    goal_daily = models.CharField(max_length=50, default="run for 20 minutes")
    goal_date = models.DateTimeField(default=datetime.date.today)

    def __str__(self):
        return "Goal"

