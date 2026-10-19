user = {
    "name": "Babu",
    "age": 25,
    "city": "Delhi"
}

print(user["name"])

user["salary"] = 50000

user["age"] = 26

for key, value in user.items():
    print(key, value)