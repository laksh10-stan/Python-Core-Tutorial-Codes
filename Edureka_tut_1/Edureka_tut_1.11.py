#Classes and Objects  (OOPS)
class MyClass:
    x=4       #called properties and not values
p1=MyClass
print(p1.x)
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p2 = Person("John", 41)

print(p2.name)
print(p2.age)
#Class is an object constructor
