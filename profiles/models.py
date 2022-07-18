from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile", null=True)#when profile is deleted, user is not but not vice versa
    goal = models.IntegerField(blank=True, null=True)
    goal_date = models.IntegerField(blank=True, null=True)
    
    def __str__(self):
        return self.user.username + ' profile'