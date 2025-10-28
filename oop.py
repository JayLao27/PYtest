class dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return "Woof!"
    
    def birthday(self):
        self.age += 1
        return f"Happy birthday {self.name} Age: {self.age}"

    def get_info(self):
        return f"Dog name: {self.name}, Age: {self.age}"


mahdog = dog("Yosh", 3)


print(mahdog.bark())
print(mahdog.birthday())
print(mahdog.get_info())
