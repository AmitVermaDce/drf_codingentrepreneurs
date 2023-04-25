import requests
import pprint

endpoint = "http://127.0.0.1:8000/api/products/77/"


response = requests.get(endpoint)
pprint.pprint(response.json()) 

 