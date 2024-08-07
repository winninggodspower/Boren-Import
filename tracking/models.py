from django.db import models

# Create your models here.
class Tracker(models.Model):
    tracker_id = models.CharField(unique=True, max_length=50)
    tracking_number = models.CharField(unique=True, max_length=50)