#looping
#two types .......1-->while....2-->for
i=1
while i<=6:
    print(i)
    i+=1
i=1
print('\n')
while i<=6:
    print(i)
    if i==4:
        break
    i+=1
print('\n')
i=0
while i<6:
    i += 1
    if i==4:
        continue
    print(i)
artists=['Eminem','Pink','Machine Gun Kelly','Linkin Park']
for x in artists:
    print (x)
for x in '21 Pilots':
    print(x)
for x in artists:
    if x =='Machine Gun Kelly':
        break
    print(x)
print('\n')
for x in artists:
    if x =='Machine Gun Kelly':
        continue
    print(x)
for x in range(6):
    print(x)
print('\n')
for x in range(2,7):     #2 is not included but 7 is
    print(x)
print('\n')
for x in range(0,99,9):     #0 to 99 with once in every 9 iteration
    print(x)
print('\n')
for x in range(2,7):     #2 is not included but 7 is
    print(x)
else:
    print('Finally Finished')
print('\n')
names=['Marshall','Pink','Colson','Chester Bennington']
for x in artists:     #2 is not included but 7 is
    for y in names:
         print(x,y)
print('\n')
def tri_recursion (k):
    if k>0:
        result=k+tri_recursion(k-1)
        print(result)
    else:
        result=0
    return result
print('\nRecursion Result\n')
tri_recursion(6)

