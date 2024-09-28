from django.contrib import admin

from core.models import Gallery
from .models import CustomerFX, Procurement, RiskAttestation

# Register your models here.
admin.site.register(CustomerFX)
admin.site.register(Procurement)
admin.site.register(RiskAttestation)
admin.site.register(Gallery)
