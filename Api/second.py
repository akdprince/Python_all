#This is we try to post some data to a API

import requests

url = "https://jsonplaceholder.typicode.com/posts"

payloads = {
    "title": "Hello from Python to ANIK",
    "body": "This is first time i'm posting a data to API",
    "UserId":1,
    "id": 101
}

response = requests.post(url, json=payloads)

print("Status Code: ", response.status_code)
data = response.json()
print(data)