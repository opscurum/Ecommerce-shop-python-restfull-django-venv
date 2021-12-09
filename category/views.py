from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status, permissions

from .models import Category, CategorySerializer
from rest_framework import viewsets
from rest_framework.decorators import api_view

# Create your views here.


class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Category to be viewed or edited.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
