# Object-Oriented Programming, William Castengera, v0.1

class Person:# Use PascalCase for ClassNames
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

        # To string function --- how the object appears as a string
        def __str__(self):
            return f"Name: {self.name}\nThis person is {self.age} years old.\nThey weigh {self.weight} pounds.\n"


person1 = Person("John D. Sugma", 74, 350)
print(person1)