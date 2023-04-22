from django.http import JsonResponse
from django.forms.models import model_to_dict
import json
from products.models import Products

# Create your views here.

def api_home(request, *args, **kwargs):
    model_data = Products.objects.all().order_by("?").first()
    data = {}
    if model_data:
        data = model_to_dict(model_data, fields=["title","content", "price"])
    return JsonResponse(data=data)