#tuple......unlike lise it is unchangeable
tuple1 = ("Jaime","Cersie","tyrion")
print(tuple1)
print(tuple1[1])
#tuple1[1]="Danny"           .......tuples cant be changed
print(tuple1)
for x in tuple1:
    print(x)
if "Jaime" in tuple1:
   print("Yes Jaime Exist")
else:
    print("Jaime has been wiped out")
print(len(tuple1))
#del tuple1
#print(tuple1)
newtuple = tuple(("Bear Grylls","Brady Barr","Austin Stevens"))   #Constructor not a normal list
print(newtuple)
#...........other funcs of tuple .......count(),index()