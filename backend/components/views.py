from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.serializers import ProductsSerializer
from products.models import Products
from django.http import JsonResponse


# Create your views here.
@api_view(["POST"])
def api_home(request, *args, **kwargs): 
    '''
    DRF API View
    '''
    serializer = ProductsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        data = serializer.data
        return JsonResponse(data) 