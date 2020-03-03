'''
Difference between procedure oriented programming (POP) and Object oriented programming (OOPS)
POP                                                                         |        OOP
1. In POP, program is divided into small parts called functions.            |1. In OOP program is divided into parts called objects.
2. POP follows top-down approach.                                           |2. OOP follows bottom-up approach.
3. In POP, data can move freely from a function to function in the system.  |3. In OOP objects can move and communicate with each other through member functions.
4. Examples--> C, VB, FORTRAN, PASCAL                                       |4. Examples--> C++, JAVA and Python
'''
'''
OOPS Concepts
Creating and using classes and objects becomes easy
Data becomes active
Code is reusable thus, less code needs to be written
Ability to simulate real world events more accurately
Faster, accurate and better written applications
'''
'''
Difference between python OOP and other OOPs
1. You can't write a single piece of code in JAVA without using class, but you can do so in Python, even many projects don't use it.
2. Python is an interpreted language, means it execute code line-by-line, if your code has some error, that error will be shown when your line of code will be executed,
that's not the case with JAVA.
'''
'''
Class is a blueprint used to create objects having same property or attribute as its class.
An object is an instance of a class which contains variables and methods.
1. A class is a template for objects. It contains the code for all the object's methods.
2. A class describes the abstract characteristics of a real-life thing.
3. An instance is an object of a class created at run-time.
4. There can be multiple instances of a class
'''
class number():
    pass
x = number()
print(x)
class Edureka():
    def Hello(self):
        print("Happy Ending")
ob=Edureka()
ob.Hello()
'''
SCOPE OF VARIABLES (IN CONTEXT OF CLASS)
1. GLOBAL --> The variables which are declared outside the class and can be used anywhere in the program.
2. LOCAL -->
'''
b=12
class demo():
    a=89
print(b) #global variable b
#print(a)            it'll throw an error since a is a local variable
print(demo.a)        #this'll work
'''
ATTRIBUTES
Class attributes which are owned by class itself. They will be shared by all the instances of the class.
1--> BUILT-IN ATTRIBUTES      (meta data)
2--> USER DEFINED ATTRIBUTES
-->attributes are created inside the Class definition
-->We can dynamically create new attributes for existing instances of a Class
'''
class Edureka:
    '''
    This is the docstring
    '''
    count=0
print('Edureka.__dict__:',Edureka.__dict__)              #dictionary containing the class's namespace
print('Edureka.__doc__:',Edureka.__doc__)                #class documentation string or none if undefined
print('Edureka.__name__:',Edureka.__name__)              #class name        ....uses--> large systems, frameworks
print('Edureka.__module__:',Edureka.__module__)          #module name in which the class is defined
print('Edureka.__bases__:',Edureka.__bases__)            #a possibly empty tuple containing the base classes, in order of their occurrence in the base class list
class Foo(object):
    def math(self):
        pass
'''
TYPES OF ATTRIBUTES
1. Private---> These can only be accessed inside of the Class definition
2. Public----> These can and should be, freely used
3. Protected-> These are accessible only from within the class of its subclasses

'''
class New():
    def __init__(self):
        self.__pri = ("I'm private" )             #private----> Double Underscore "__"
        self._pro = ("I'm protected" )            #protected--> Single Underscore "_"
        self.pub = ("I'm public" )                #public ----> No Underscore
ob=New()
print(ob.pub)
print(ob._pro)              # it's against the rules of protected variable but still it works because python is somewhat flexible or liquid than JAVA
#print(ob.__pri)            # this won't work but there's another way of accessing private variable
class MyClass:
    def myPublicMethod(self):
        print('Public Method')
    def __myPrivateMethod(self):
        print('this is private method')
obj=MyClass()
obj.myPublicMethod()
#obj.__myPrivateMethod()   # this'll throw an error as private method can't be accessed outside the class
'''
ACCESSING PRIVATE METHODS
We can access private methods by using one underscore with class name "_ClassName"
'''
class MyClass1:
    def myPublicMethod1(self):
        print('Public Method')
    def __myPrivateMethod1(self):
        print('Private Method')
obj1=MyClass1()
obj1.myPublicMethod1()
obj1._MyClass1__myPrivateMethod1()              #that's how you access a private method
class New1:
    domain=('Data Science')
    def Setcourse(self,name):
        self.name=name
ob1=New1()             #instance of class New1
ob2=New1()             #instance of class New1
ob1.Setcourse('Python')
ob2.Setcourse('Machine Learning')
print(ob1.domain)             #class variable is shared by both instances
print(ob2.domain)             #class variable is shared by both instances
print(ob1.name)               #instance variable is unique to each instance
print(ob2.name)               #instance variable is unique to each instance
'''
CONSTRUCTOR AND DESTRUCTOR

'''
class Test:
    def __init__(self):                   # CONSTRUCTOR is implemented using __init__(self) which you can define parameters that follows the self
        print('Constructor')
    def __del__(self):                    # DESTRUCTOR is defined using __del__(self). In the example, the obj2 is created and manually deleted, therefore, both messages will be displayed.
        print('Destructor')
if __name__ == '__main__':
    obj2=Test()
    del obj2
'''
MULTIPLE CONSTRUCTORS
Use--> Same kind of class in different ways
'''
class Date:
    def __init__(self, year, month, day):
        self.year=year
        self.month=month
        self.day=day
    @classmethod                     #decoratotor-->passes the cls or the self object
    def dmy(cls,day,month,year):
        cls.year=year
        cls.month=month
        cls.day=day
        return cls(cls.year, cls.month, cls.day)
    @classmethod
    def mdy(cls,month,day,year):
        cls.year=year
        cls.month=month
        cls.day=day
        return cls(cls.year,cls.month,cls.day)
a=Date(2016,12,11)
print(a.year)
b=Date.dmy(9,10,2015)
print(b.year)
a=Date.mdy(7,8,2014)
print(a.year)