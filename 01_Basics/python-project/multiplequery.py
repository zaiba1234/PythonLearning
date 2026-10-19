import requests

url = "https://example.com/api/products"

params = {
    "category": "shoes",
    "page": 1,
    "limit": 10
}

response = requests.get(url, params=params)

print(response.url)