from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("account/", include("account.urls")),
    path("", include("home.urls")),
    path("orders/", include("orders.urls")),
    path("products/", include("products.urls")), 
]