import requests
import pprint

endpoint = "http://127.0.0.1:8000/api/products/44/"


response = requests.get(endpoint)
pprint.pprint(response.json()) 

 