from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Item
from .serializers import ItemSerializer

'''
NOTE: Conside this as a reference and follow this same coding structure or format to work on you tasks
'''

# Create your views here.
class ItemView(APIView):

    def get(self, request):
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def menu_list(request):
    menu = [
        {"name": "Margherita Pizza", "description": "Classic cheese and tomato pizza", "price": 350},
        {"name": "Veg Burger", "description": "Burger with fresh Veggies and cheese", "price": 200},
        {"name": "Pasta AlFredo", "description": "Creamy white sauce pasta", "price": 300},
    ]
    return Response(menu)