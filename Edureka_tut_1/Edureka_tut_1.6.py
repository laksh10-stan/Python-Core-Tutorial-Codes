#python dictionaries
#unordered, changeable, indexed
dict1={'Brand':'Lamborghini','Year':2016,'Model':'Aventador'}
print(dict1)
x = dict1["Brand"]
print(x)
y = dict1.get("Year")
print(y)
dict1['Model']='Murcelago'
print(dict1)
for x in dict1:
    print(x)
for x in dict1:
    print(dict1[x])
for x in dict1.values():
    print(x)
for x,y in dict1.items():
    print(x,y)
if 'Year' in dict1:
    print("Year Exist")
print(len(dict1))
dict1['Color']='Red'
print(dict1)
dict1.pop('Year')
print(dict1)
dict1.popitem()
print(dict1) #deleted last key
#del dict1        ..............Error.......
#print(dict1)
dict1.clear()
print(dict1)
dict1 = dict(Brand='Marussia',Year='2019',Model='Dortmund')
print(dict1)
#other methods...........clear(),copy(),fromkeys(),get(),items(),keys(),update(),pop()