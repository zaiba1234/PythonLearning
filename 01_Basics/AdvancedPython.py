square = lambda x: x * x

print(square(5))

numbers = []

for i in range(5):
    numbers.append(i * 2)

    numbers = [i * 2 for i in range(5)]


    # def numbers():
    # for i in range(5):
    #     yield i

check = lambda x: "Even" if x % 2 == 0 else "Odd"

print(check(10))
print(check(7))


maximum = lambda a, b: a if a > b else b

print(maximum(10, 20))

students = [
    ("Rahul", 80),
    ("Amit", 95),
    ("Neha", 70),
    ("Priya", 90)
]

students.sort(key=lambda x: x[1])

print(students)



numbers = [1, 2, 3, 4, 5]

squares = [x * x for x in numbers]

print(squares)


# Create even numbers

# 1 se 20 tak ke even numbers list comprehension se nikalo.


even_numbers = [x for x in range(1, 21) if x % 2 == 0]

print(even_numbers)


# lambda arguments: expression


add = lambda a, b: a + b

print(add(10, 20))

multiply = lambda a, b: a * b

print(multiply(5, 4))



check = lambda x: "Even" if x % 2 == 0 else "Odd"

print(check(10))
print(check(7))



check = lambda x: "Even" if x % 2 == 0 else "Odd"

print(check(10))
print(check(7))


# List Comprehension

numbers = []

for i in range(5):
    numbers.append(i * 2)

print(numbers)


# List Comprehension with Condition:Normal way:


numbers = [1, 2, 3, 4, 5, 6]

even_numbers = []

for x in numbers:
    if x % 2 == 0:
        even_numbers.append(x)

print(even_numbers)

# Comprehension:

numbers = [1, 2, 3, 4, 5, 6]

even_numbers = [x for x in numbers if x % 2 == 0]

print(even_numbers)



numbers = range(1, 11)

odd_numbers = [x for x in numbers if x % 2 != 0]

print(odd_numbers)


# Dictionary Comprehension

# Normal:
numbers = [1, 2, 3, 4, 5]

squares = {}

for x in numbers:
    squares[x] = x * x

print(squares)

# Using comprehension:

numbers = [1, 2, 3, 4, 5]

squares = {x: x * x for x in numbers}

print(squares)


# With condition
numbers = range(1, 11)

even_squares = {
    x: x * x
    for x in numbers
    if x % 2 == 0
}

print(even_squares)



# Set Comprehension:

# A set stores unique values.


numbers = [1, 2, 2, 3, 3, 4, 5]

unique = {x for x in numbers}

print(unique)


# Generator

# A generator produces values one at a time instead of storing everything in memory.

def numbers():
    return [0, 1, 2, 3, 4]

def numbers():
    for i in range(5):
        yield i

#  result = numbers()
# for number in result:
#     print(number)


# yield
# yield is used to create generators.
def count():
    yield 1
    yield 2
    yield 3

result = count()

print(next(result))
print(next(result))
print(next(result))

# Why Generator?

# Imagine you need:

# numbers = list(range(10000000))

# This stores millions of numbers in memory.

# Generator:
def numbers():
    for i in range(10000000):
        yield i
        
        # It generates values when needed.
#
# This is useful for:

# Large files
# Large datasets
# Data processing
# Machine learning pipelines
# APIs
# Streaming data


# Decorator
# A decorator allows you to modify or extend a function without changing its original code.

def my_decorator(func):

    def wrapper():
        print("Before")

        func()

        print("After")

    return wrapper

def hello():
    print("Hello")

    # Now create a function:
    
    # def hello():
    # print("Hello")

    # Apply decorator:

    # hello = my_decorator(hello)
    #  hello()

    