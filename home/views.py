from django.conf import settings
from django.shortcuts import render

# Create your views here.
def home(request):
    context = {
        return render(request, 'home.html', {
        "restaurant_address": settings.restaurant_address
    })
    