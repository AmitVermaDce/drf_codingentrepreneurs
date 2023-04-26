import requests
import pprint
from getpass import getpass

auth_endpoint = "http://127.0.0.1:8000/api/auth/"
password = getpass()
auth_response = requests.post(auth_endpoint, json={
    'username': 'staff',
    'password': password,
})
print(auth_response.json())

if auth_response.status_code == 200:
    endpoint = "http://127.0.0.1:8000/api/products/"
    token = auth_response.json()['token']
    headers = {
        "Authorization": f"Bearer {token}"
    }
    response = requests.get(endpoint, headers=headers)
    print(response.json())

