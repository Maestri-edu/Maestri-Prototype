from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("pix/", include("pix.urls")),
    path("pix-slip/", include("pix_slip.urls")),
    path("hook/", include("hook.urls")),
]
