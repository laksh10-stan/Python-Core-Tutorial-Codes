'''
MODULES AND EXCEPTION HANDLING
STANDARD LIBRARIES--> Collection of tools that come with with python.
                      It includes-->
                      1. Built-in-functions
                      2. Modules
                      3. Packages
'''
'''
MODULES
1. It allows you to logically organize the code.
2. They are basically python files with .py extension.
3. A Module is a file containing Python definition and statements.
-->Use "import" to tell Python to load a module. When the interpreter encounters an import statement, it imports the Module, if it is present in the search path.
--> From Import statement allows you to import specific attribute from specific module into the current namespace.
Dir Function
A dir is built-in function which returns the list of strings containing the name defined by the Module. It gives the list of variables, functions defined in that module.

'''
import math
print(dir(math))
from math import sqrt              #More recommended,  Less memory required
print(sqrt(4))
print(dir(sqrt))
'''
"import*" --> It allows you to import all the attributes from the required module This provides an easy way to import all the items from a module into the current namespace.
'''
from math import*                 #Less recommended because the module can have a variable with same name as the variable in your code and it can cause runtime error i.e. wrong output.
print(cos(pi/3))
'''
RELOAD FUNCTION
When the module is imported into a script, the code in the top-level portion of a module is executed only once. Therefore, if you want to re-execute the top level code in a module, you can use the reload function. The reload function imports a previously imported module again.
'''
'''
IMPORTANT MODULE
1. Sys
2. Os
3. Math
4. DateTime
5. Random
6. Json
'''
'''
Sys Module---> Deals with Operating system interactions, not much useful for data science.
This module provides access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter. It is always available
'''
import sys
print(sys.argv)                #Stores any command line argument passed, when you start python. Also includes name of program.
#print(sys.exit())             #Tells the python interpreter to quit.
print(sys.winver)              #Returns the version number used to form registry keys on Windows platform.
print(sys.flags)               #Returns the struct sequence flags exposes the status of command line flags.
print(sys.prefix)              #Returns a string giving the site specific directory prefix where the platform independent python files are installed.
print(not sys)                 #returns False if module is imported, else True.
'''
Os Module--> Its also related to os interactions
The "os" module includes the code that lets python work with your operating system, that even run operating system commands.
'''
import os
print(os.getcwd())
print(os.chdir('E:/Python'))          #Changes the directory
print(os.mkdir('E:/Python/Py'))       #Creates directory in given path
print(os.rmdir('E:/Python/Py'))       #Removes directory from given path
print(os.name)                        #Returns the name of the operating system dependent module imported
print(os.environ)                     #Returns a mapping object representing a string environment
print(os.getlogin())                  #Returns the name of the user logged in on the controlling terminal of the process
print(os.getcwd())                    #Returns the current working directory
print(os.getppid)                     #Returns the parent's process id
print(os.chdir('E:/colors'))
print(os.getcwd())
'''
Os.path Module

'''
print(os.chdir('C:Users\Lakshmendra Singh\.PyCharmCE2018.3\config\scratches\Edureka_tut_2'))
print(os.path.join('E:\Python','E:\Python'))          #It takes one or more paths and joins them by using the current operating system's path separator.
print(os.path.abspath('Edureka_tut_2.11.py'))         #It takes a relative pathname and returns the corresponding absolute pathname.
print(os.path.normpath('Edureka_tut_2.3.py'))         #It converts path names from non-standard format to standard format.
print(os.path.normpath('\Edureka_tut_2.3.py'))        #It converts path names from non-standard format to standard format.
print(os.path.normpath('..\Edureka_tut_2.3.py'))      #It converts path names from non-standard format to standard format.
print(os.getcwd())
print(os.path.split('C:Users\Lakshmendra Singh\.PyCharmCE2018.3\config\scratches\Edureka_tut_2\Edureka_tut_2.8.py'))      #It takes a pathname and returns it in two parts: the directory part and the filename.
print(os.path.exists('E:\Python\kuchbhi.txt'))                                                                            #It takes a pathname and returns true if it exist.
print(os.path.isdir('E:\Python'))                                                                                         #It takes a pathname and returns true if it points to a directory.
print(os.walk('C:Users\Lakshmendra Singh\.PyCharmCE2018.3\config\scratches\Edureka_tut_2'))                               #It will generate tuple of path, folders, files present in given path and will keep on traversing the sub-folders.
print(os.getcwd())
for i in os.walk('E:/Python/New folder (2)'):
    print (i)
'''
Math Function

'''
print(math.ceil(0.145))
print(math.floor(1.76))
print(math.copysign(12,-8))       #Returns 12 with the sign of Minus (-)
print(math.fabs(-19.4))
print(math.exp(5))                #e**5
print(math.expm1(2))              #e**2 - 1
print(math.log(100,10))           #log x to the base y
print(math.acos(0.5))             #Returns the arc cosine of x in radians
print(acos(0.5))
print(math.asin(0.5))             #Returns the arc sine of x in radians
print(math.atan(5))               #Returns the arc tangent of x in radians
print(math.cos(3))                #Returns the cosine of x in radians
print(degrees(22/7))              #Converts radians to degrees
print(radians(180))               #Converts degrees to radians
print(pi)                         #Returns 3.14
print(e)                          #Returns 2.718
'''
Random Module
This Module implements pseudo-random number generators for various distributions.
'''
import random
num1 = random.randrange(100)            #Returns random integer between 0 and 100
print(num1)
num2=random.randrange(-11,12)           #Returns random integer between -11 and 12
print(num2)
num3=random.randrange(10,1100,100)      #Returns random integer between 10 and 1100 with step of 100
print(num3)
num4=random.randint(0,30)               #Returns a random integer N such that a<=N<=b
print(num4)
print(random.getstate)                  #Returns an object capturing the current internal state of the generator
print(random.uniform(6,2))              #Returns a random floating point number N such that a<=b and b<=N<=a for b<a
print(random.uniform(2,90))             ##Returns a random floating point number N such that a<=b and b<=N<=a for b<a
'''
Applications of Random Module
1.For encrypting banking session on the internet.
2.For simulating possible rainfall we make a computerised model for estimating the environmental impact of building a dam.
3.To randomly allow a new enemy spaceship to appear and shoot at you.
4.One Time Passwords (OTP)
5.Casino websites
6.Game Building
6.Machine learning
'''
'''
DATE TIME MODULE
The datetime module includes tools for working with dates, times and combinations.
The time module includes tools for working with times and dates in the recent past to the near future.
'''
import datetime
print(datetime.datetime.today())
now=datetime.datetime.today()
other=datetime.datetime(1995,3,12,22,10)
print(now-other)
print(datetime.timedelta(18901,55547,4210000))
print(now-other)
print(datetime.MAXYEAR)             #Returns 9999 i.e. largest year allowed in a date or datetime object
print(datetime.MINYEAR)             #Returns 1   i.e. smallest year allowed in a date or datetime object
print(datetime.time)                #Returns time object with hours, minutes, seconds and microseconds
print(datetime.timezone)            #Returns a timezone object
'''
JSON (JavaScript Object Notation)
-->Lightweight format for for storing and transporting data.
-->Used to send data from server to webpage.
-->It is self describing and easy to understand.
JSON Module
It provides an easy way to encode and decode data in JSON.

'''
import json
data={'name':'acer','shares':1200,'price':1280}
json_str=json.dumps(data)              #It has a different type than dictionary
print(json_str)
print(type(json_str))
'''
Regular Expressions
1.Find a kind of data in a large amount of data.   Search, find, replace etc
A regular expression is a special text string for describing a search pattern.
Steps.
1. Find a word in a string.
2. Generate an iterator.
3. Match one of any of several letters.
4. Match series of range of characters.
4. Replace String.
5. Match a Single Character.
'''
'''
The replace method of strings is used to replace all occurrences of one string with another, and the index method is used to find the first occurrence
of a substring in a string. But sometimes you need to do a more a sophisticated search or replace the Regular Expression is used.
'''
import re
#sub-->substitution
print(re.sub(r'[ad]','*','abcde abcedf,abcdef',))          #We can use square brackets to indicate that we only want to match certain letters, It replaces every a and d with asterisks.
print(re.sub(r'abc','*','abcdef abcdef'))                  #Replaces all occurrences of abc with *
print(re.sub(r'[abcd][1234]','*','a1dsfdvmb3sf'))          #first char can be a|b|c|d and second character can be 1|2|3|4
print(re.sub('A.B','*','A1BdsafjA0BdzklvfnAaB'))           #first char must be A and second character can be anything and third character must be B.
print(re.sub('AB+','*','AB   aABBBBB AC'))                 #first character must be A and then followed y n number of B
print(re.sub(r'AB{2,4}','*','AB ABB ABBB ABBBB ABBBBB'))   #first character must be A followed by B within 2 to 4 no. of times.
print(re.sub('^abc','*','abcsdhdscfnabc'))                 #start with abc
print(re.sub('abc$','*','abcsdhdscfnabc'))                 #end with abc
print(re.sub('abc','*','abcsdhdscfnabc'))                  #either start or end with abc
#searching
print(re.search('ab','Here is an absolute string'))        #Looks for pattern anywhere in the string.
print(re.match('ab','Here is an absolute string'))         #Looks for pattern in the beginning of string.
'''
Applications
Email validation
Phone no. validation
'''
