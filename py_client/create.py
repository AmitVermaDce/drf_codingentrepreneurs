import requests
import pprint

endpoint = "http://127.0.0.1:8000/api/products/create/"

data = {
    "title": "This field is newly added",
    "content": "Text added"
}

response = requests.post(endpoint, json=data)
pprint.pprint(response.json()) 

 