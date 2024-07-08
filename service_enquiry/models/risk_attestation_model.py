from django.db import models

class RiskAttestation(models.Model):
    # Personal Information
    person_name = models.CharField(max_length=100)
    person_address = models.TextField()
    person_landmark = models.CharField(max_length=100)
    person_phone = models.CharField(max_length=15)

    # Guarantors Information
    guarantor_name = models.CharField(max_length=100)
    guarantor_address = models.TextField()
    guarantor_landmark = models.CharField(max_length=100)
    guarantor_phone = models.CharField(max_length=15)

    # Supplier Details
    supplier_name = models.CharField(max_length=100)
    supplier_address = models.TextField()
    supplier_phone = models.CharField(max_length=15)
    amount_currency = models.CharField(max_length=3, choices=[('USD', 'USD'), ('EUR', 'EUR'), ('NGN', 'NGN')])
    amount_to_pay = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.person_name} - {self.supplier_name}"
