class dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return "Woof!"

    def get_info(self):
        return f"{self.name} is {self.age} years old."

    def birthday(self):
        self.age += 1
        return self.age


mahdog = dog("Yosh", 3)


print (mahdog.birthday())
print(mahdog.bark())

print(mahdog.get_info())
