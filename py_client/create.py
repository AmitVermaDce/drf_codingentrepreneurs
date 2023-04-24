import requests
import pprint

endpoint = "http://127.0.0.1:8000/api/products/"

data = {
    "title": "This field is required."
}

response = requests.post(endpoint, json=data)
pprint.pprint(response.json()) 

 