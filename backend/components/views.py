from django.forms.models import model_to_dict
from products.models import Products
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(["GET"])
def api_home(request, *args, **kwargs):
    '''
    DRF API View
    '''
    model_data = Products.objects.all().order_by("?").first()
    data = {}
    if model_data:
        data = model_to_dict(model_data, fields=["title","content", "price"])
    return Response(data=data) 