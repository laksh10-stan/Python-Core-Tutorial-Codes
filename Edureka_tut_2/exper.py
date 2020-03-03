import random
a=input("Enter a number between 0 and 20: ")
c=int(a)
print(c)
num4=random.randint(0,20)               #Returns a random integer N such that a<=N<=b
#print(num4)
while num4!=c:
    if num4>c:
        num4=random.randint(0,num4)
        #if num4==c:
        #    break
       # print(num4)
    elif num4<c:
        num4=random.randint(num4,20)
       # if num4 == c:
       #     break
       # print(num4)
   # elif num4 == c:
   #     print(num4)
print(num4)