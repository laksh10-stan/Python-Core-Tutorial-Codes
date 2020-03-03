'''
This is multi line comment
yeah it works
'''
print('hakuna',"matata")
#identifier
'''
Naming Conventions
Class-Camelcase
identifier starts with 1 underscore ---->private
identifier starts with 2 underscores ---->strongly private
identifier starts with 2 underscores and ends with 2 underscores---->language defined special name
special characters @!#$%^&*() are not allowed in python identifiers
'''
__a=89
_b=34
__er__=90
print(__er__)
print(_b)
print(__a)
'''
......................standard data types.....................
values can be changed.................................values cant be changed
immutable..............................................mutable
numbers...strings...tuples..............................lists...dictionaries...sets
'''
a=34       #.......this is possible .......not mutation
a=45       #........what it means is 34 and 45 are different things ........a is just an identifier....you cant convert 45 to 34....ie immutable
'''
            1-->int (signed integers)
numbers.... 2-->float(Real numbers)
            3-->complex numbers
                          1-->Binary
number representation---> 2-->Decimal
                          3-->Hexadecimal
'''
a=-34
b=-34.456
c=3+56j
d=34-11j
print(a,b,c-d,a+b,b+c,b+c*d)
'''
python doesnt support char
python doesnt differntiate b/w ' and "
tuple------>fixed list
'''
tuple1=(2,5,7)
print(tuple1[0])
#............list[1]=34............#tuple dont support assignment
list1=[1,23.45,23+34j,'JKL']
print(list1[1])
print(list1)
list1[1]=-23.45
list2=[[1,23.45,23+34j],('JKL',67)]
print(list2)
print(list2[0][1])
list2[0][1]=23
#list2[1][1]=23
'''
tuples are faster lists are slower
tuples () lists[]
tuples are immutable list are mutable
'''
dict1={'age':53,'sex':'male','name':'pablo'}     #dictionaries are more readable
print(dict1['age'])
'''
unordered,unique
'''
'''
operators
1-->arithmetic ........+,-,*,?,%.**,//
2-->assignment..........=,+=,-=,*=,/=,**=,//=
3-->comparision.........==,!=,>,<,>=,<=
4-->logical.............and,or,not
5-->bitwise.............&,|,^,~,<<,>>
6-->identity............is,is not
7-->membership..........in,not in
'''
#arithmetic
a=3**2    #exponential
print(a)
d=a//2    #floor division
print(d)
#assignment
#comparision
a,b=2,3
print(a==b)
print(a!=b)
#logical
print(a and b)
print(a or b)
print (not a)
print(not True)
print(not False)
print(True and False)
print(True or False)
print(not 1)
#bitwise
#identity
a=5
print(5 is 4)
print(a is 5)
print(5 is a)
print(a is a)
print(5 is not 2)
print(5 is not a)
print(a is not a)
today = 'Thursday'
yoga_day='Friday'
print(today is yoga_day)
tuple3=(12,45,567)
print(12 in tuple3)
print(12 not in tuple3)
list3=[12,11,'hakka']
print('hakka' in list3)
dict3={'age':53,'sex':'male','name':'pablo'}
print('age' in dict3)
print('pablo' not in dict3)          #only for keys and not for data