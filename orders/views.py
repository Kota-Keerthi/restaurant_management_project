from django.shortcuts import render
from .models import Restaurant
# Create your views here.

def home(request):
    restaurant = Restaurant.objects.first()
    return render(request, 'home.html', {
        'restaurant_name': restaurant.name if restaurant else "Our Restaurant"
    })
