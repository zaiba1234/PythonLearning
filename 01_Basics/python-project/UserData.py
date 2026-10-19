# import requests

# url = "https://jsonplaceholder.typicode.com/users"

# response = requests.get(url)

# users = response.json()

# print(users[0])

# print(users[0]["username"])

# print(users[0]["email"])



# import requests

# url = "https://jsonplaceholder.typicode.com/users"

# response = requests.get(url)

# users = response.json()

# for user in users:
#     print(user["id"], user["name"], user["email"])




import requests

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)

if response.status_code == 200:
    print("API Success")
    print(response.json())
else:
    print("API Failed")