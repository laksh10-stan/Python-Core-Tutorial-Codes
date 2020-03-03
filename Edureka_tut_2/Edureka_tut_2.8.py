from functools import reduce
'''
BUILT-IN FUNCTIONS --> These are built into (already available) in python  and canbe accesed by end users
Examples-->
sorted()         -->     returns a new sorted list from the items in iterable
abs()            -->     returns the absolute value of an integer, floating point or complex number
all()            -->     returns True if all elements of the supplied iterable are true
any()            -->     converse of all() function
globals()        -->     returns a dictionary representing the current global symbol table
bin()            -->     converts an integer number to a binary string prefixed with "0b"
bool()           -->     converts a value to boolean using standard Python truth testing procedure
enumerate()      -->     returns an enumerate object with items and thei index values
eval()           -->     the arguments are string and optional globals and locals. If provided, globals must be a dictionary. If provided locals can be any mapping object.
chr()            -->     returns the string representing a character whose unicode point is the integer
int()            -->     returns an integer object constructed from a number or string x
sum()            -->     sum(iterable) sums the numeric values in an iterable such as list tuple or set
open()           -->     opens a file and return a corresponding file object
len()            -->     returns the length of an object
reversed()       -->     reversed(seq) is a reverse iterator on a object of the type that you can loop through and process. The list and tuple types are supported with this function.
'''
#print(sum(int(23,16)))
print(sorted([12,45,1,-34.33,221]))
print(all([True,True,'True',1,2,45,-56]))
print(all([True,False,'True',1,2,45,-56]))
print(all([True,'True',1,2,45,-56,0]))
print(all([True,'True',1,2,45,-56,None]))
print(any([True,None,0]))
print(any([False,None,0]))
print(bool(False))
print(bool(0))
print(bool(None))
print(bool(True))
print(bool(1))
print(bool('Hakka noodle'))
print(chr(67))
print(chr(97))
print(chr(95))
print(abs(-88))
print(abs(33+89j))
print(int('124'))
#print(int('kakka'))       # wont do anything
print(len([1,2,3,4]))
print(len('abcdwer'))
print(bin(123))
print(bin(-123))
print(sum([1,2,3]))
print(sum((1,2,3)))
print(sum({1,2,3}))
print(reversed([1,2,3]))   # wont work we'll have to use loop
for i in reversed([1,2,32,-1]):
    print(i)
grocery =['bread','sauce','pan']
enumerateGrocery =enumerate (grocery)
print(type(enumerateGrocery))
print(list(enumerateGrocery))                # it'll print tuples with index starting from 0
enumerateGrocery=enumerate(grocery,10)
print(list(enumerateGrocery))                # it'll print tuples with index starting from 0
'''
LAMBDA function
Lambda functions are used if we want to make our functions more concise, easy to write and read
Anonymous lambda function can be defined using keyword lambda
They can't contain commands and they can't contain more than one expression
They can take any no. of arguments (including optional arguments)
It allows us to pass other function as a parameter
'''
ans = (lambda z:z*4)  #this is doing multiplication by 4 in 1 line i.e. MORE CONCISE
print(ans(7))
def mult4(a):         #this is doing multiplication by 4 in 2 lines
    return a*4
print(mult4(7))
items=[1,2,3,4]
squared = list(map(lambda x: x**2, items))                       #MAPPING
print(squared)
number_list = range(-5,5)
less_than_zero = list(filter(lambda x: x<0, number_list))        #FILTERING
print(less_than_zero)
product = reduce((lambda x, y: x*y),[1,2,3,4])                   #REDUCTION
print(product)
'''
SCOPE OF VARIABLES
1. Global
Definition--> The variables which are not declared in the function and can be used anywhere in the program


2. Local
Definition--> The variables which are declared within the function and can be used only inside that fuction

'''
a=90       #global variable
def sum(b):
    n=80
    print('n=',n)
    sum = b+n
    print('Addition is: ', sum)
print(a)
sum(23)
#print(n)            this'll throw an error as n is a local variable
a=12
b=11
print(id(a))      #returns the address
print(id(b))
'''
FUNCTION ARGUMENTS
The no. of arguments in the function call should match exactly with the Function definition
KEYWORD ARGUMENTS
when you use Keyword arguments in a function call, the caller identifies the argument by the parameter name
'''
def welcome(str):
    print("Welcome to python ",str)
    return()
welcome(str='Phoebe')
def func1(a,b,c,d):
    sum=a**d+c**b
    return(sum)
print(func1(a=2,b=4,c=2,d=1))    # this way of calling a function is more preferred since the order of arguments doesn't matter anymore
'''
DEFAULT ARGUMENTS
Definition--> A Default argument is an argument, that assumes a default value if a value is not provided in the Function call for that argument
'''
def func2(a,b,c,d=3):   #here d=3 is a default value
    sum=a**d+c**b
    return sum
print(func2(a=2,b=4,c=2))
def func3(a,b,c,d=3):   #here d=3 is a default value
    sum=a**d+c**b
    return sum
print(func3(a=2,b=4,c=2,d=19))    #if we pass d here as well as default value then the value here will be used  i.e. default calue is only used when no. value is passed
'''
VARIABLE LENGTH ARGUMENTS
You may want to process a Function for more arguments than you have specified while defining the function, so you can use the variable length arguments
EXAMPLE--> Multiplication function of calculator program where we don't know weather the user's gonna multiply 2 nos., 3 nos. etc.
'''
def info(user,*users):
    print('Users of python:')
    print(user)
    for var in users:
        print('Users of python ')
        print(var)
        return()
info('annie')
info('Deobrah','Noah')
info('Alex','Daniel','Jorah')
def use(user,*users):
    print('First user argument',user)
    for user in users:
        print('User received from variable length argument',user)
use('admin','org','Cyborg','Pulga')
def func4(arg1, arg2, arg3, *args, **kwargs):
    print('First normal argument: ' + str(arg1))
    print('Second normal argument: ' + str(arg2))
    print('Third normal argument: ' + str(arg3))
    print('Non-keyword argument: ' + str(args))
    print('Keyworded argument: ' + str(kwargs))
func4(1,2,3,4,5,6,7,name='Alex',surname='Daniel',age=90)             #just like polymorphism