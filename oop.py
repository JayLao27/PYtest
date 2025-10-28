class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return "Woof!"

    def get_info(self):
        return f"{self.name} is {self.age} years old."


# create an instance of Dog (outside the class)
mahdog = Dog("Yosh", 3)
print(mahdog.bark())
print(mahdog.get_info())
