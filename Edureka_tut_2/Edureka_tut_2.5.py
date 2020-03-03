#sequences
'''
Sequences are containers that are accessible by indexing aur slicing.
The built-in len() function takes any container as argument and returns the no. of items in the container
'''
'''
operations
1.concatenation
2.repetition               ....    i.e.multiplication
3.membership testing
4.slicing            ..........  cutting a portion ...........[index1 - index4] .....1 is included 4 is not
5.indexing
'''
list1=['Hadoop','Python','Java']
print(list1[1])
print(list1[0:2])        #slicing
print(list1[-1])         #runs from backwards
print(list1+['Angular','PHP','MongoDB'])      #concatenation
print(list1*3)        #repetition
print('Hadoop' in list1, 'Java' in list1)
'''
Types of sequences in python
1. lists
2. tuples
3. strings
4. sets
5. sets
6. dictionaries
'''