from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)#when profile is deleted, user is not but not vice versa
    name = models.CharField(max_length=100, null=True)
    age = models.IntegerField(blank=True, null=True)
    rate = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True)
    

    def __str__(self):
        return self.user.username + ' profile'