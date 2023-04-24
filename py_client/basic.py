import requests
import pprint

endpoint = "http://127.0.0.1:8000/api/"


response = requests.post(endpoint, json={"title": "Hello World"})
# json data is the body data in byte string format --> b'{"query": "Hello world!!"}'
pprint.pprint(response.json()) 

 