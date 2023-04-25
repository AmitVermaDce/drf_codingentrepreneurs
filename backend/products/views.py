from .models import Products
from .serializers import ProductsSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from django.http import Http404

@api_view(["GET", "POST"])
def products_alt_view(request, pk=None, *args, **kwargs):
    method = request.method
    if method == 'GET':
        if pk is not None:
            # detail view
            obj = get_object_or_404(Products, pk=pk)  
            data = ProductsSerializer(obj, many=False).data       
            return Response(data=data)
        # List view
        queryset = Products.objects.all()
        data = ProductsSerializer(queryset, many=True).data
        return Response(data)
    
    if method == "POST":
        serializer = ProductsSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            title = serializer.validated_data.get("title")
            content = serializer.validated_data.get("content") or None
            if content is None:
                content = title
            serializer.save(content=content)
            return Response(serializer.data)
        return Response({"invalid": "Not a good data"}, status=400)
    