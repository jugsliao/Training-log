from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile", null=True)
    goal = models.TimeField(blank=True, null=True)
    goal_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.user.username + "Profile"

    # def save(self):
    #     super().save()
    #     weeks_to_goal = (self.goal_date - datetime.now()) / 7

