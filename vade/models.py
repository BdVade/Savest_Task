from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime, timedelta



# Create your models here.

class User(AbstractUser):
    pass


class UserMetrics(User):
    class Meta:
        proxy = True

    time_threshold = datetime.now() - timedelta(hours=24)
    users_added_today = User.objects.filter(date_joined__lt=time_threshold).count()
    users_added_this_week = User.objects.filter(date_joined__lt=datetime.now() - timedelta(days=7))
    users_added_this_month = User.objects.filter(date_joined__lt=datetime.now() - timedelta(days=30))


