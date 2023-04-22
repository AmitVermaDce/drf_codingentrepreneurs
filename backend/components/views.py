from django.http import JsonResponse
import json

# Create your views here.

def api_home(request, *args, **kwargs):
    # It gives us url query parameters
    print(request.GET)
    print(request.POST)
    body = request.body
    data = {}
    try:
        data = json.loads(body)
    except:
        pass 
    data['params'] = dict(request.GET)
    data['headers'] = request.headers  
    data['content_type'] = request.content_type
    print(data)
    return JsonResponse({"message": "Hello there, I am coming from api...."})