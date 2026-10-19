# print("Hello Babu")
# print("Hello Rahul")
# print("Hello Amit")


def greet(name):
    print(f"Hello {name}")

greet("Babu")
greet("Rahul")
greet("Amit")


def add(a, b):
    return a + b

result = add(10, 20)

print(result)


def greet(name="User"):
    print(f"Hello {name}")

greet()
greet("Babu")