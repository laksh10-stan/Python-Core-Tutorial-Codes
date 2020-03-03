temp=50
try:
    temp=temp/0
except ZeroDivisionError:
    print('Cant divide by zero', end = "")
else:
    print('Division Successful', end="")
try:

    temp=temp/5
except:
    print('Inside Except block',end="")
else:
    print('Edureka',end="")