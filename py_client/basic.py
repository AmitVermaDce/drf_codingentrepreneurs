import requests

endpoint = "http://127.0.0.1:8000/api/"


response = requests.get(endpoint, params={"abc": 123}, json={"query": "Hello world!!"})
# json data is the body data in byte string format --> b'{"query": "Hello world!!"}'
print(response.json()['message']) 

 