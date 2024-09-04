from django.urls import path
from . import views

urlpatterns = [
    path('', views.submitted_forms, name="submitted_forms"),
    path('detail/procurement/<form_id>', views.procurement_form_detail, name="procurement_detail"),
    path('detail/fxs/<form_id>', views.fx_form_detail, name="fxs_detail"),

]
