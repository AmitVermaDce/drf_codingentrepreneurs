from rest_framework import generics
from .models import Products
from .serializers import ProductsSerializer

# DetailView give one item at a time    
class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer