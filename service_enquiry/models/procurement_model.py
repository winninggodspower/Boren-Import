from django.db import models
from user_authentication.models import User

class Procurement(models.Model):
    CATEGORY_CHOICES = [
        ('category1', 'Category 1'),
        ('category2', 'Category 2'),
    ]
    CUSTOMER_TYPE_CHOICES = [
        ('type1', 'Type 1'),
        ('type2', 'Type 2'),
    ]
    CURRENCY_CHOICES = [
        ('USD', 'USD'),
        ('EUR', 'EUR'),
        ('NGN', 'NGN'),
    ]
    PAYMENT_METHOD_CHOICES = [
        ('credit_card', 'Credit Card'),
        ('paypal', 'PayPal'),
    ]

    # link to user
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    customer_type = models.CharField(max_length=100, choices=CUSTOMER_TYPE_CHOICES)
    payment_currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES)
    payment_method = models.CharField(max_length=100, choices=PAYMENT_METHOD_CHOICES)
    purchase_order_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    title = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    other_names = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=255)
    nearest_landmark = models.CharField(max_length=255)
    type_of_order = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField()
    social_media = models.CharField(max_length=50, blank=True, null=True)
    social_media_handle = models.CharField(max_length=50)
    recipient_name = models.CharField(max_length=100)
    business_name = models.CharField(max_length=100, blank=True, null=True)
    mailing_address = models.CharField(max_length=255)
    state = models.CharField(max_length=50, blank=True, null=True)
    zip_code = models.CharField(max_length=10, blank=True, null=True)
    mailing_phone_number = models.CharField(max_length=15, blank=True, null=True)
    agree = models.BooleanField(default=False)

    date_submitted = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.purchase_order_name