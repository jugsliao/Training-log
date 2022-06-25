import datetime
from time import time

from django.db import models
from django.utils import timezone
from django.contrib import admin
from django.contrib.auth.models import User

# Create your models here.
class Log1(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) #when profile is deleted, user is not but not vice vers
    time1 = models.CharField(max_length=50)
    time2 = models.CharField(max_length=50)
    time3 = models.CharField(max_length=50)
    time4 = models.CharField(max_length=50)
    time5 = models.CharField(max_length=50)
    time6 = models.CharField(max_length=50)
    pub_date = models.DateTimeField('date published')

    @admin.display(
        boolean=True,
        ordering='pub_date',
        description='Published recently?',
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    def __str__(self):
        return self.user.username + " log"

