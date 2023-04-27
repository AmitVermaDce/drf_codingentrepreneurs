from rest_framework import viewsets
from .models import Products
from .serializers import ProductsSerializer
from rest_framework.generics import mixins

class ProductViewSet(viewsets.ModelViewSet):
    '''
    get -> list -> Queryset
    get -> retrieve -> Product Instance Detail View
    post -> create -> New Instance
    put -> Update
    patch -> Partial Update
    delete -> destroy
    '''
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    lookup_field = "pk" # default


class ProductGenericViewSet(
        mixins.ListModelMixin,
        mixins.RetrieveModelMixin,
        viewsets.GenericViewSet):
    '''
    Perform specific tasks from this class
    Only doing Listing and Detailing views
    '''
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    lookup_field = 'pk'

# product_list_view = ProductGenericViewSet.as_view({'get': 'list'})
# product_detail_view = ProductGenericViewSet.as_view({'get': 'retrieve'})