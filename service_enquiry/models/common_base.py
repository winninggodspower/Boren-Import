from django.db import models
from user_authentication.models import User

class CommonFieldsBase(models.Model):
    CURRENCY_CHOICES = [
        ('USD', 'USD'),
        ('EUR', 'EUR'),
        ('NGN', 'NGN'),
    ]
    PAYMENT_METHOD_CHOICES = [
        ('credit_card', 'Credit Card'),
        ('bank_transfer', 'Bank Transfer'),
        ('paypal', 'PayPal'),
    ]

    # link to user
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    payment_method = models.CharField(max_length=50, choices=PAYMENT_METHOD_CHOICES)
    
    date_submitted = models.DateTimeField(auto_now=True)
    tracking_number = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.surname} {self.first_name}"