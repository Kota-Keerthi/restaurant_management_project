from django.urls import path
from .views import menu_list, home

urlpatterns = [
    path('', home, name='home'), 
    path('api/menu/', menu_list, name='menu-list'),
]