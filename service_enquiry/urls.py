
from django.urls import path
from . import views

urlpatterns = [
    path("procurement_form", views.procurement_form, name="procurement_form")
]
