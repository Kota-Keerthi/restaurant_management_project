from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')
from django.conf import settings
from django.shortcuts import render

def home(request):
    context = {
        "restaurant_name": settings.restaurant_name,
        "restaurant_address": settings.restaurant_address
    }
    return render(request, "home.html", context)
    