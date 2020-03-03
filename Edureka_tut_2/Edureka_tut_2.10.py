'''
OOPS
Abstraction---->
1.Simplifying complex reality by modeling classes appropriate to the problem
2.Class Abstraction means to separate class implementation from the use of the class
Encapsulation-->
1.Combining the code into a public interface, and aprivate implementation of that interface.
2.Mechanism for restricting the access to some of an object components, this means that the internal representation of an object cannot be seen from outside of the objects definition.
Inheritance---->
1.Very powerful feature of OOP
2.It refers to deriving a class from the base class with little or no modification in it
A-Single inheritance
B-Multiple Inheritance
C-Multilevel Inheritance
Overriding----->You can always override your parent class methods. One reason for overriding parent's ,method is because you may want special or different functionality in your subclass.
Polymorphism--->
'''
class Base1:
    def fun(self):
        print('In class base 1')
class sub(Base1):                           #inheritence
    def fun(self):
        print('In sub')                     #this has more priority
    pass
ob=sub()
ob.fun()
'''
Multiple Inheritance
'''
class First(object):
    def __init__(self):
        super(First,self).__init__()
        print('first')
class Second(object):
    def __init__(self):
        super(Second,self).__init__()
        print('second')
class Third(Second,First):
    def __init__(self):
        super(Third,self).__init__()
        print('Third')
Third()
'''
Multilevel inheritance
'''
class Animal:
    def eat(self):
        print('eating')
class Dog(Animal):
    def bark(self):
        print('Barking')
class BabyDog(Dog):
    def weep(self):
        print('Weeping')
d=BabyDog()
d.weep()
d.bark()
d.eat()
class Parent:
    def myMethod(self):
        print('Calling parent method')
class Child(Parent):
    def myMethod(self):
        print('Calling child method')
c=Child()                    #Child overrides the method written in parent Class
c.myMethod()
'''
CLASS OVERRIDING
'''
class Rectangle():
    def __init__(self,ln,br):
        self.ln=ln
        self.br=br
    def Area(self):
        print(self.ln*self.br, "is the area of rectangle")
class Sq(Rectangle):
    def __init__(self,side):
        self.side=side
        Rectangle.__init__(self,side,side)
    def Area(self):
        print(self.side*self.side,'is the area of square')
s=Sq(4)
r=Rectangle(2,7)
s.Area()
r.Area()
'''
POLYMORPHISM
It is the abilty to leverage the same interface for different underlying forms such as data types or classes.
It is an important feature of class definition in Python that is utilized when tou have commonly named methods across classes or subclasses.
'''
class Ani:
    def talk(self):
        pass
class Horse(Ani):
    def talk(self):
        print('Neigh')
class Monkey(Ani):
    def talk(self):
        print("Chirp")
h=Horse()
h.talk()
m=Monkey()
m.talk()
'''
SETTER AND GETTER METHODS
THe methods used for changing the values of attributes are called Setter Methods.
The methods used for retrieving or accessing the values of attributes are called Getter Methods.
USE-->SECURITY
'''
class Ano:
    def __init__ (self,cname):
        self.cname=cname
    def scName(self,cname):
        self.cname=cname
    def getcName (self):
        return(self.cname)
ob=Ano('Pyth')
print(ob.getcName())
ob.scName('ML')
print(ob.getcName())