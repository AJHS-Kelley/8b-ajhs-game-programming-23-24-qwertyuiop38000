# Object-Oriented Programming, William Castengera, v0.1

class Person:# Use PascalCase for ClassNames
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

        # To string function --- how the object appears as a string
    def __str__(self):
        return f"Name: {self.name}\nThis person is {self.age} years old.\nThey weigh {self.weight} pounds.\n"

    def classFunction(self):
        print("this is an example class function\n")
        print("It only works when called on an object of that class")



person1 = Person("John D. Sugma", 74, 350)
person2 = Person("John D. ligma", 76, 360)
# print(person1)
# print(person2)

# if person1.weight > person2.weight:
#     print(f"{person1.name} weighs more than {person2.name}\n")
# elif person1.weight == person2.weight:
#     print("Each person weighs the same.\n")
# else: 
#     print(f"{person2.name} weighs more than {person1.name}\n")

# if person1.age > person2.age:
#     print(f"{person1.name} is older than {person2.name}\n")
# elif person1.weight == person2.weight:
#     print("Each person is the same age.\n")
# else: 
#     print(f"{person2.name} is older than {person1.name}\n")


# person1.classFunction()

# Changes properties after creation
print(person1.name)
person1.name = "Jack the ripper"
print(person1.name)

# Deleting Properties

print(person1.name)
del person1.name
print(person1)