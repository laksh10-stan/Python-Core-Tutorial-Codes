'''
Types of sequences in python
1. lists
            ...opertions--> slicing, updating, deleting, length, concatenation, repetition
            ...applications--> 1. data that doesnt need random access, 2. data thatcan be changed
2. tuples
3. strings
4. sets
5. sets
6. dictionaries
'''
list1 = ['MongoDB','Hadoop','AngularJS']
#list1[3]='Kamikaze'      ......will pose out of index error
list1[2]='Kamikaze'     #updating
print(list1)
del(list1[1])    #deletion
print(list1)
list1 = ['MongoDB','Hadoop','AngularJS','Kinshasha','Hakuna Matata']
print(list1.pop(2))  #returns element a index 2 .....but also removes it
print(list1)
print(list1.remove('Kinshasha'))       #just removes an element doesnt return anything
print(list1)
print(type(list1))     #returns the type of data type
list2=[1,3,5,7,9]
for x in list2:
    print (x**2)
print([x**3 for x in [2,4,6,8]])
print(list2)
list2.append('Pochinki')       #adds one item at the end
print(list2)
list2.extend(['Rashford','Lukaku']) #adds more than one item at the end
print(list2)
list2.insert(2,'La Pulga') #adds an item at agiven index
print(list2)
list2.remove('Rashford') #removes a paricular item
print(list2)
list3=[9,11,13.5,12,90,11.0,11,-13.001,2**2]
print(sorted(list3))
list4=['Howitzer','TSAR Bomba','ICBM','Cherokee']
print(sorted(list4))
print(list4)
list4=sorted(list4)
print(list4)
for course in list4[::-1]:        #prints reverse order of list without actually reversing the list
    print (course)
print(list4)
list5 = [[1,4.2,56],['Kepa','De Gea']] #list within a list
print(list5)
list6 = [(1,4.2,56),['Kepa','De Gea'],{'Pablo':'Escobar','Joey':'Tribianni','Ross':'Geller'}]  #list.tuple and dictionary inside list
print(list6)
print(len(list6))
print(list6[1][0:2])
print(list6[2]['Joey'])
#   list6[0][1]=23   ...this will throw an error because an immutable item wont become mutable even if it's used inside mutable sequence i.e. tuple inside list will remain immutable
print(list6)
'''
Part 2
Tuples
immutable ---> cant be changed
operations ---> slicing, updating, deletion, length, concatenation
faster ---> less execution time
application --> where you have to deal with data that can be changed i.e. immutable ......examples  --> pi, scientific constants...etc
start with regular brackets " () " and contents are separated by comma " , "
'''
tup1 = (1,-56,23**2,2,45)
print(len(tup1))
print(max(tup1))
print(min(tup1))
tup2 = ('Manga','Doraemon','Pokemon','Sinchan','Hagemaru')
print(len(tup2))
print(max(tup2))   # max will be the one with maximum ASCII value in this case "Sinchan"
print(min(tup2))
'''
tup3 = ('Manga','Doraemon','Pokemon','Sinchan','Hagemaru',9,120000)   # this isn't working i don't know know why
print(len(tup3))
print(max(tup3))
print(min(tup3))
'''
print(sorted(tup2))
for course in tup1[::-1]:        #prints reverse order of tuple without actually reversing the list
    print (course)
print(len(tup2))            #returns length of tuple
print(tup1*2)               #repetitiion
print('Doraemon' in tup2)   #membership checking
tup4 = (1,5,7,2,0)
tup5 = (2.4,67,12,-0)
tup6 = tup4 + tup5
print(tup6)
# del (tup4) this will throw an erroe as tup4 isn't defined and u cant delete something which isn't defined
# print(tup4)
tup7 = ((1,34,56),[12,34,546],{1:'Itzhak Stern',2:'Oscar Schindler',3:'Dwayne Pretorious'})  #tuple, list, dictionary inside tuple
print(len(tup7))
print(tup7[0][0:3])
tup7[1][1]=11      #as we are using list inside the tuple thus, it can be updated i.e. it has become mutable
print(tup7)        #tup7[1] is immutable but tup7[1][1] is mutable
del(tup7[1][1])    #as we are using list inside the tuple thus, it can be deleted i.e. it has become mutable
print(tup7)
tup8=('Bahrouzaan','Dembele',43,2**3,'Moussa')
lst=list(tup8) #conversion of tuple to list
print(lst)
lst[1]='Boa'
print(lst)
tup9=tuple(lst)   #conversion of list to tuple
print(tup9)
print(list(tup9))
'''
3.Strings
created by enclosing in double quotes ("") or single quotes ('') or triple quotes (""" """)
operations --->
1. slicing
2. updating
3. concatenation
4. repetition
5. membership testing
6. reverse
its something like tuple
but it cant store lists, tuples or dictionaries inside them
it contains alphanumeric
'''
str1='Kukoo'
str2="Gaitonde"
str3="""Pikachu"""
print(str1)
print(str2)
print(str3)
print(len(str1))
print(str2[1:4])
print('t' in str1)
#string=('P','Y','T','H','O','N')
#string='Python'
#string[0]='j'          it'll throw an error because string doesn't support individual item assignment just like tuples
'''
placeholders in python
just like fill in the blanks

'''
course='Hadoop'
name='Jim Carrey'
age=23
print('Welcome to %s' %(course))
print('My name is %s and my age is %d' %('Slim Shady',22))
print('Welcome to ' +course+ '. Have a nice day')     #this is messy
print('Welcome to %s. Have a nice day' %(course))     #this is convenient
print('My name is %s and my age is %d' %(name,age))   #this is convenient
print('My name is '+name+' and my age is '+str(age))  #str conversion is necessary that's why this method is not preferred
'''
%c              character
%s
%i              signed decimal integer
%d
%u              unsigned decimal integer
%o              octal integer
%x              hexadecimal integer lowercase letters
%e              exponential notation with lowercase 'e'
%f              floating point real number
%g              the shorter of %f and %e
%G
%X
%E
'''
str1='hakunanana'
print(str1.capitalize())            #capitalize first letter of the string
print(str1.count('na',0,len(str1)))
s=str1.encode('utf-8','strict')     #returns encoded string version of string
print(s)
print(max(str1))
print(min(str1))
print(str1.replace('a','--A--',1))      #replaces all occurrences of old in string with new or at most max occurences if max is given
print(str1.upper())                     #converts lowercase letters in string to uppercase
print(str1.index('a'))                  #same as find but raises an exception if string not found
print(str1[::-1])
print(str1[2:6])
print(str1.find('a'))                   # will give -1 if it doesn't find anything ........it won't show any error
str2 ='Wadakkam'
print(str1+str2)
print(str2*2)
'''
4.Sets
unordered collection of unique items
defined by values separated by comma inside braces "{}"
sets can also be created by built-in set function
uses ---> 1. if we want to collect unique strings or ints from a sequence
          2. creating IDs, passwords (uniqueness)

SET OPERATIONS
A- Union operation --> union of A and B is a set of elements from both sets. Union is performed using | operator.
For Example --> A={2,5,1,7,2,1}
                B={4,9,1,2,6,9}
                print(A|B)
                output =(1,2,4,5,6,7,9)
B- Intersection --> Intersection of A and B is a set of elements that are common in both sets. Intersection is performed using & operator
For Example --> A={2,5,1,7,2,1}
                B={4,9,1,2,6,9}
                print(A&B)
                output =(1,2)
C- Difference --> Difference of A and B (A - B) is a set of elements that are only in A but not in B, similarly B-A is a set of elemnts in Bbut not in A
For Example --> A={2,5,1,7,2,1}
                B={4,9,1,2,6,9}
                print(A-B)
                output =(5,7)
OTHER OPERATIONS
1. Membership testing
'''
set1={'Ken','Wrath','Paolo'}
print(set1)
x=set('welcome')  #doesn't repeat any item even when it occurs more tha once i.e. 'e' in welcome
print(x)
A={2,5,1,7,2,1}
B={4,9,1,2,6,9}
print(A|B) #Union
print(A&B) #Intersection
print(A-B) #Difference
s={1,2,3,'a','b'}
set1={1,'a','b'}
print(1 in s)
print(set1.issubset(s))
print(5 not in s)
print(s.issuperset(set1))
print(s.union(set1))
print(s.intersection(set1))
print(s.difference(set1))
print(s.symmetric_difference(set1))
s.add('c')
print(s)
s.remove(2)  # it'll throw an error if 2 is not present inside the set s. In other words it just removes item from the set weather it is present or not.
print(s)
s.discard(3) # it won't throw an error if 2 is not present inside the set s. In other words it just removes item from the set only if it is present inside the set.
print(s)
s.pop()      # removes and returns an arbitrary element from the list
print(s)
s.clear()    # removes all elements from the list
print(s)
'''
5. DICTIONARIES
Definition--> unordered collection of key-value pairs.
Dictionaries are mutable.
uses--> when we have large amount of data, real life situation.
Example--> Details about a person.
Operations
A- length
B- membership testing
C- del
'''
dict1 = {1:'Black Mamba',2:'King Cobra',3:"Russel's Viper"}
print(dict1)
print(dict1[1])
person = { 'name' : 'Xavier Doherty',
           'age' : 39,
           'sex' : 'male',
           'nationality' : 'Australian'
}
print(person['name'])     #more readable as a developer
dict1[1]='Inland Taipan'  #updatation
print(dict1)
del(dict1[3])             #deletion
print(dict1)
print(len(dict1))         #returns no. of keys i.e. length of dictionary
print(str(dict1))         #Returns dictionary as a string. Useful in web development, also if you're using Json package
print(type(dict1))        #Returns type
print(person.get('city')) # it'll return none if 'city' doesn't exist, but it won't throw any error. you can't use this with 'if' condition if 'city' doesn't exist.
print(person.items())     #retuns items(keys + values) of dictionary
print(person.keys())      #returns keys of dictionary
print(person.copy())      #creates a copy of the dictionary
print(person.clear())     #deletes all the elements in dictionary
print(person)
person = { 'name' : 'Xavier Doherty',
           'age' : 39,
           'sex' : 'male',
           'nationality' : 'Australian'
}
for key in person:       # dictionaries are unordered so it'll print keys randomly
    print(key)
for key in sorted(person.keys()):
    print(key)
dict2 = {1:(1,2,3),2:(4,5,6),3:(7,8,9)} #tuples as dictionary items
print(dict2)
print(dict2[1][1])
dict2 = {1:(1,2,3),2:[4,5,6],3:{7,8,9}} #tuples, lists, dictionaries  as dictionary items
print(dict2)
print(dict2[2][0])

