from django.db import models

# Create your models here.
class Newsletter(models.Model):
    email = models.EmailField(max_length=254, unique=True)

    def __str__(self):
        return self.email
    

    @classmethod
    def send_mass_email(subject, body):
        pass
