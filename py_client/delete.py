import requests
import pprint

product_id = input("What is the product id?")
try:
    product_id = int(product_id)
except:
    product_id = None
    print(f"{product_id} is not a valid id....")

if product_id:
    endpoint = f"http://127.0.0.1:8000/api/products/{product_id}/delete/"
    response = requests.delete(endpoint)
    pprint.pprint(response.status_code) 




 