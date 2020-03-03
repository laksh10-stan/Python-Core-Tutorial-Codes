'''
PACKAGES IN PYTHON
A package is a collection of python modules. Python packages allow you to break down large systems and organize their modules in a consistent way that
you and other people can use and reuse efficiently.
'''
'''
EXCEPTION HANDLING
It is a signal, occurs when an error or other unusual condition has occurred.
Exceptions are handled using atry statement. A critical operation, which can raise exception is placed inside the try clause and the code that handles exception is written in except clause.
Errors:
1. ValueError
2. TypeError
3. ZeroDivisionError
'''
#a=23/0        #this is an exceptional event
import sys
randomlist=['a',0,23]
for entry in randomlist:
    try:
        print('The entry is ',entry)
        r=1/int(entry)
        break
    except:
        print('OOPS!',sys.exc_info()[0],'occurred')
        print('No Entry')
        print()
print('The reciprocal of ',entry, 'is ', r)
'''
Finally block
The try statement in python can have optional finally clause. This clause is executed no matter what, and is generally used to release external resources.
'''
try:
    f=open("test.txt",encoding= 'utf-8')
finally:                                                   #it is used for memory cleanup, closing large files etc.
    f.close()
'''
try:
    fh=open('testfile.txt','w')
    fh.write('This is my test file for exception handling')
except:
    print('Error:cant find file or read data')
finally:
    fh.fclose()
'''
'''
USER DEFINED EXCEPTIONS
Programmers may name their own exceptions by creating a new exception class.
Exceptions need to be derived from the Exception class, either directly or indirectly.
'''
class Error(Exception):
    pass
class ValueSmallError(Error):
    pass
class ValueLargeError(Error):
    pass
number=10
while True:
    try:
        in_num=int(input('Enter a number: '))
        if in_num < number:
            raise ValueSmallError
        elif in_num > number:
            raise ValueLargeError
        break
    except ValueSmallError:
        print('This Value is too small, try again!')
        print()
    except ValueLargeError:
        print('This Value is too large, try again!')
        print()
print('Congratulations! you guessed it correctly')
