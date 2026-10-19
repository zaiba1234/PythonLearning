import requests

url = "https://jsonplaceholder.typicode.com/users"

params = {
    "id": 1
}

response = requests.get(url, params=params)

print(response.url)
print(response.json())