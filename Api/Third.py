# This is for access twitter now X post create and delete thourgh api

import requests

TOKEN = "AAAAAAAAAAAAAAAAAAAAAE415gEAAAAALGdZEj3Ayf1IkksjjhfHleb%2FmJI%3DjE3fVarwTmONi" #private token for your profile
BASE_URL="https://api.x.com/2/users/by/username/TechWithTimm" 

headers = {
    "Authorization": f"Bearer {TOKEN}"
}

response = requests.get(BASE_URL, headers=headers)

print("Status code:", response.status_code)
print("URL:", response.url)

try:

    data = response.json()
    print(data)
except ValueError:
    print("Response is not JSON:")
    print(response.text)