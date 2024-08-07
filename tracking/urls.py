from django.urls import path
from . import views

urlpatterns = [
    path('submit/', views.submit_tracking, name='tracking_form'),
    path('details/<str:tracking_number>/', views.tracking, name='tracking_details'),
]
