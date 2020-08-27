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
    result = User.objects.filter(date_joined__lt=time_threshold).count()


