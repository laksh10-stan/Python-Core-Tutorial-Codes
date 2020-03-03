#FUNCTIONS AND OOPS
'''
Functions ---> block of organized, reusable code that is used to perform a single and related action
use--> section of code to be used multiple times

'''
num = int(input('Number: '))
factorial=1
if num<0:
    print('Must be positive')
elif num==0:
    print('Factorial = 1')
else:
    for i in range(1,num+1):
        factorial=factorial*i
print(factorial)
'''
Function declaration and definition
'''
def add(a,b):
    sum = a+b
    return (sum)
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
ans=add(num1, num2)
print('%d + %d = %d' %(num1, num2, ans))
ans2=add(23,45)                                    #reusability
print('23 + 45 = %d' %(ans2))
print(add(12,34))                                  #reusability
