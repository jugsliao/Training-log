import datetime
from time import time

from django.db import models
from django.utils import timezone
from django.contrib import admin
from django.contrib.auth.models import User

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

