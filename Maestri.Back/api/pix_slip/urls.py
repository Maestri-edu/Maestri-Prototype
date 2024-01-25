from django.urls import path
from . import views

urlpatterns = [
    path("payment", views.create_payment),
    path("payment-response", views.payment_response),
]
