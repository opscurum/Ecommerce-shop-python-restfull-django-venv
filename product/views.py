from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status

from .models import Product, ProductSerializer
from rest_framework import viewsets, permissions
from rest_framework.decorators import api_view


# Create your views here.

class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
