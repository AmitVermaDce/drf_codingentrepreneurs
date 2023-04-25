import requests
import pprint

endpoint = "http://127.0.0.1:8000/api/products/23/update/"

data = {
    "title": "Title is updated",
    "price": 7999.99
    
}

response = requests.put(endpoint, json=data)
pprint.pprint(response.json()) 

 