from django.contrib import admin
from .models import Menu, Order, UserProfile

admin.site.register(Menu)
admin.site.register(Order)
# Register your models here.
admin.site.register(UserProfile)
 python manage.py runserver