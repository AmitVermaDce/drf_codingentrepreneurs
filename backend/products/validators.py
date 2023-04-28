from .models import Products
from rest_framework import serializers

def validate_title(value):
    qs = Products.objects.filter(title__exact=value)
    if qs.exists():
        raise serializers.ValidationError(f"{value} is already a product name...")
    return value