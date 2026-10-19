class User:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"My name is {self.name}")


        user1 = User("Babu", 25)

# user1.introduce()