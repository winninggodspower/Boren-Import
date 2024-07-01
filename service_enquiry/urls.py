
from django.urls import path
from . import views

urlpatterns = [
    path("procurement_form", views.procurement_form, name="procurement_form"),
    path("customer_fx_form", views.customer_fx_form, name="customer_fx_form")
    path("risk_attestation_form", views.views.risk_attestation_form, name="risk_attestation_form")
]
