from datetime import datetime

from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class staff(models.Model):
    id = models.AutoField(primary_key=True)
    s_name = models.CharField(max_length=32)
    s_mobilenumber = models.CharField(max_length=64, unique=True)
    s_isworking = models.BooleanField(default=False)


class hours(models.Model):
    id = models.AutoField(primary_key=True)
    h_name = models.CharField(max_length=32, null=True)
    start_time = models.CharField(max_length=32, default=datetime.now)
    end_time = models.CharField(max_length=32, default='')
    hours_today = models.CharField(max_length=16, default=0)
    record_date = models.DateField(auto_now_add=True)
