from django.db import models
from product.models import Product

from rest_framework import serializers

# Create your models here.

class Slider(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.IntegerField(default=0, blank=True)

    class Meta:
        ordering = ['order']


class SliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slider
        fields = ['order', 'product']
