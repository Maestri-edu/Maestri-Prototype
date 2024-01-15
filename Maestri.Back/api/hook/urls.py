from django.urls import path
from . import views

urlpatterns = [
    path("pix", views.create_hook_pix),
    path("pix_slip", views.create_hook_pix_slip),
]
