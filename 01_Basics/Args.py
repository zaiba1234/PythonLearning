# # 🔟 *args

# # *args allows a function to accept multiple positional arguments.


# def add(a, b):
#     return a + b

# print(add(10, 20))

# # But what if we want:

# add(10, 20, 30, 40, 50)



def add(*args):

    total = 0

    for number in args:
        total += number

    return total

print(add(10, 20))
print(add(10, 20, 30))
print(add(10, 20, 30, 40, 50))

