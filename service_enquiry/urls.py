
from django.urls import path
from . import views, chat_views

urlpatterns = [
    path("procurement_form", views.procurement_form, name="procurement_form"),
    path("customer_fx_form", views.customer_fx_form, name="customer_fx_form"),
    path("risk_attestation_form", views.risk_attestation_form, name="risk_attestation_form"),

    # chat urls
    path('fetch_messages/<int:chat_id>/', chat_views.fetch_messages, name='fetch_messages'),
    path('send_message/<int:chat_id>/', chat_views.send_message, name='send_message'),
    path('stream_messages/<int:chat_id>/', chat_views.stream_messages, name='stream_messages'),
]
