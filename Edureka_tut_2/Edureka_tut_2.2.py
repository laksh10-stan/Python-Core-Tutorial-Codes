import sys
#conditional statements
'''
1---> if
2=-> elif
3--> else
1 tab = 4 white spaces
'''
x=12
y=23
if(x<y):
    print(x)
    print('Heheheeh')
if(x>y):
    print('Bhak')
else:
    print('aww')
if(x>y):
    print('lop')
elif(x<y<12):
    print('Erwin')
else:
    print('Puskas')
'''
loop
1-->while
2-->for
3-->nested
'''
c=0
while c<2:
    print(c)
    c+=1
fruits=['Grapes','Mangoes','Apples','Bananas']
for i in fruits:
    print(i)
'''
break---> come out of th nearest loop
continue--> skip current iteration of loop
pass-->when a statement is required syntactically but you dont want any command or code to execute
'''
for i in [1,2,6,87]:
    pass
print('kick kich')
'''
command line arguments
.argv refers to no. of args passed
argv[] is a pointer array which points to each argument which is passed to main
the python sys module provides access to any command line arg via the sys.argv ...this serve 2 purposes:
1-->sys.argv is the list of command line args
2-->len(sys.arg) is the no. of command line arguments
'''
print(len(sys.argv))


print(sys.argv)


