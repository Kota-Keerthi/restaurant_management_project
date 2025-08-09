from django.conf import settings
from django.shortcuts import render

# Create your views here.
def home(request):
    context = {
        "restaurant_name": settings.restaurant_name,
        "restaurant_address": settings.restaurant_address
    }
    return render(request, "home.html", context)
    