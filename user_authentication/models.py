from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
     
    phone = models.IntegerField(null = True)

    user_img = models.ImageField(upload_to='USERIMG/',blank=True)

    def __str__(self): # __unicode__ on Python 2
        return self.username