from django.db import models
from user_authentication.models import User

class CustomerFX(models.Model):
    CATEGORY_FX_CHOICES = [
        ('category1', 'Category 1'),
        ('category2', 'Category 2'),
    ]
    TRANSACTION_TYPE_CHOICES = [
        ('type1', 'Type 1'),
        ('type2', 'Type 2'),
    ]
    PAYMENT_METHOD_CHOICES = [
        ('credit_card', 'Credit Card'),
        ('bank_transfer', 'Bank Transfer'),
        ('paypal', 'PayPal'),
    ]
    CURRENCY_CHOICES = [
        ('USD', 'USD'),
        ('EUR', 'EUR'),
        ('NGN', 'NGN'),
    ]

    # link to user
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # FX Transaction Details
    category_fx = models.CharField(max_length=50, choices=CATEGORY_FX_CHOICES)
    transaction_type = models.CharField(max_length=50, choices=TRANSACTION_TYPE_CHOICES)
    payment_method = models.CharField(max_length=50, choices=PAYMENT_METHOD_CHOICES)
    transaction_number = models.CharField(max_length=50)

    # Sender Information
    sender_title = models.CharField(max_length=50)
    sender_surname = models.CharField(max_length=50)
    sender_first_name = models.CharField(max_length=50)
    sender_other_names = models.CharField(max_length=50, blank=True, null=True)
    sender_address = models.CharField(max_length=255)
    sender_email = models.EmailField()
    sender_amount_currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES)
    sender_amount = models.DecimalField(max_digits=10, decimal_places=2)

    # Receiver Information
    receiver_title = models.CharField(max_length=50)
    receiver_surname = models.CharField(max_length=50)
    receiver_first_name = models.CharField(max_length=50)
    receiver_other_names = models.CharField(max_length=50, blank=True, null=True)
    receiver_address = models.CharField(max_length=255)
    receiver_email = models.EmailField()
    receiver_postal_code = models.CharField(max_length=20)
    receiver_bank_address = models.CharField(max_length=255)
    receiver_account_number = models.CharField(max_length=50)
    receiver_iban = models.CharField(max_length=50)
    receiver_amount_currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES)
    receiver_amount = models.DecimalField(max_digits=10, decimal_places=2)
    transfer_reason = models.CharField(max_length=255)

    date_submitted = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.transaction_number} - {self.sender_surname} {self.sender_first_name}"