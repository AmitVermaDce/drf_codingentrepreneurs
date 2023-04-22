from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.forms.models import model_to_dict
from products.serializers import ProductsSerializer
from products.models import Products


# Create your views here.
@api_view(["GET"])
def api_home(request, *args, **kwargs):
    '''
    DRF API View
    '''
    instance = Products.objects.all().order_by("?").last()
    data = {}
    if instance:
        data = ProductsSerializer(instance).data
    data['headers'] = request.headers
    data['content_type'] = request.content_type
    data['params'] = request.GET
    return Response(data) 