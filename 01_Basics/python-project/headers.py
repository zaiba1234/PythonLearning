import requests

url = "https://example.com/api/users"

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}

response = requests.get(
    url,
    headers=headers
)

print(response.status_code)
print(response.json())