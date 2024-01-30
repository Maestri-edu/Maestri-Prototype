from django.urls import path
from . import views

urlpatterns = [
    path("pix-slip/payment", views.create_pix_slip_payment),
]
