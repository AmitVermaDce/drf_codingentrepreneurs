from .models import Products
from .serializers import ProductsSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics, mixins 
from components.mixins import (
    StaffEditorPermissionMixin, 
    UserQuerySetMixin)

class ProductCreateAPIView(
    UserQuerySetMixin,
    StaffEditorPermissionMixin, 
    generics.ListCreateAPIView):    
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer

    def perform_create(self, serializer):
        title = serializer.validated_data.get("title")
        content = serializer.validated_data.get("content") or None
        if content is None:
            content = title
        serializer.save(user=self.request.user, content=content)

    # def get_queryset(self, *args, **kwargs):
    #     qs = super().get_queryset(*args, **kwargs)        
    #     request = self.request
    #     user = request.user
    #     if not user.is_authenticated:
    #         return Products.objects.none()
    #     return qs.filter(user=request.user)

product_list_create_view = ProductCreateAPIView.as_view()


class ProductListAPIView(UserQuerySetMixin, StaffEditorPermissionMixin, generics.ListAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer

product_list_view = ProductListAPIView.as_view()


class ProductDetailAPIView(UserQuerySetMixin, StaffEditorPermissionMixin, generics.RetrieveAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer

product_detail_view = ProductDetailAPIView.as_view()


class ProductUpdateAPIView(StaffEditorPermissionMixin, generics.UpdateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title

product_update_view = ProductUpdateAPIView.as_view()


class ProductDeleteAPIView(StaffEditorPermissionMixin, generics.DestroyAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        super().perform_destroy(instance)
        
product_destroy_view = ProductDeleteAPIView.as_view()


class ProductMixinView(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    generics.GenericAPIView):

    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    lookup_field = "pk"
    
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    def perform_create(self, serializer):
        title = serializer.validated_data.get("title")
        content = serializer.validated_data.get("content") or None
        if content is None:
            content = title
        serializer.save(content=content)
    

product_mixin_view = ProductMixinView.as_view()
