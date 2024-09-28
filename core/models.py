from django.db import models

# Create your models here.
class Gallery(models.Model):
    image = models.ImageField(upload_to='gallery')
    date_added = models.DateField(auto_now=True)

    def __str__(self):
        return str(self.date_added)
