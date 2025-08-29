from django.urls import path
from .views import menu_view

urlpatterns = [
    path("contact/", contact_view, name="contact"),
    
]