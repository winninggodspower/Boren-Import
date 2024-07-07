from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
     
    phone = models.IntegerField(null = True)
    email = models.EmailField(max_length=254, unique=True)
    user_img = models.ImageField(upload_to='USERIMG/',blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self): # __unicode__ on Python 2
        return self.username