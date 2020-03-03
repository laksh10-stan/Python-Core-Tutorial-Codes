#Conditional statements
a,b,c=6,6,9
if b>a:
    print("b is badass")   #........indentation is important
elif b<a:
    print("a is badass")
else:
    print("Both are badasses")
if a == b: print('Both')            #........python Shorthand
print(b) if b>c else print(c)       #........python Shorthand
b=9
print(b) if b>c else print(c) if c>b else print('Both are eq')    #........python Shorthand
a,b,c,d=2,3,4,5
if a<b and a<c:
    print("a smallest")
if a<b or a==c:
    print("a smallest")

