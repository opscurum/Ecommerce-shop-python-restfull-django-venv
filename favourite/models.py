from django.db import models
from product.models import Product
from django.contrib.auth.models import User

from rest_framework import serializers

# Create your models here.

class Favourite(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('product', 'user')

class FavouriteSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Favourite
        fields = ['user', 'product']
