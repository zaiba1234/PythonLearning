import requests

user_id = 5

url = f"https://jsonplaceholder.typicode.com/users/{user_id}"

response = requests.get(url)

print(response.status_code)
print(response.json())