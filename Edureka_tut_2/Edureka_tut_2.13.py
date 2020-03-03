'''
INTRODUCTION TO NUMPY AND PANDAS
1.-->HUGE DATA DEALING
2.-->GEOGRAPHICAL DISTRIBUTION OF POSTS
'''
'''
DATA ANALYSIS
It is the process of inspecting, cleansing, transforming, and modelling data with the goal of discovering useful information, suggesting conclusion and supporting decision making
Raw Data--> Postprocessing (Transformation in desired format-->Clean the transformed data)-->Modelling (Prepare a model-->Analyse threads and make decisions)
'''
'''
WHY PYTHON FOR DATA ANALYSIS
Python provides various methods for data analysis, manipulation and visualization.
Data Analysis--> Numpy
Data Manipulation--> matplotlib
'''
'''
INTRODUCTION TO NUMPY
NumPy is a package for scientific computing
1.Multidimensional Arrays
2.Element by element operation
3.Methods for processing arrays
4.Mathematical operations like liner=ar algebra.
OPERATIONS IN NumPy
1. Mathematical and Logical
2. Fourier Transform and shape manipulation
3. Linear Algebra and random number generation.
'''
'''
Ndarray
The Ndarray is a multidimensional array object consisting of two parts--the actual data, some metadata which describes the stored data.
They are indexed just like sequences are in python, starting from 0.
----------------------------------------------------------------------------------------
The difference between numpy array and normal array is that of metadata.
'''
import numpy as np
a=np.array([1,2,3])
print(a)
'''
Each element in ndarray is an object of data-type object (called dtype)
An item extracted from ndarray, is represented by a python object of an array scalar type.
'''
original_array=[1,2,3,4]
a=np.array(original_array)
print(a)                                     #this won't print any comma
print(original_array)                        #this will print commas in output
print(type(a))                               #this has numpy.ndarray type
print(type(original_array))                  #this has list type
b=np.array([[12,24,36], [11,22,33]])         #this will have a matrix like output
print(b)
c=np.array([[12,24,11,36], [11,22,33]])      #this'll have a list like output
print(c)
d=np.arange(0,999)                           #Starts with 0 but 999 isn't included
print(d)
arr=np.zeros((2,3))                          #prints a 2 by 3 matrix of zeros....#its applications include scientific computing and machine learning
print(arr)
vector = np.linspace(0,20,4)                 #(start, stop, no. of steps)
print(vector)
'''
Creating arrays from existing data
'''
x=[1,233,452,11,10]
c=np.asarray(x)                              #converting an existing sequence into ndarray
print(c)
print(type(c))
'''
Restructuring a numpy array
'''
d=np.zeros(8)
print(d)
arr3d=d.reshape((2,2,2))                    #restructured array
print(arr3d)
arr3d1=d.reshape(1,8,1)                     #restructured array               #applications in machine learning
print(arr3d1)
'''
Machine Learning = maths, statistics and programming
'''
'''
Flatten a 3d array back to a single dimensional array
'''
aw=arr3d.ravel()
print(aw)
'''
Indexing of numpy arrays
'''
aq=np.arange(2,20)
print(aq)
el=aq[6]
print(el)
print(type(el))           #el is not an integer type
print(el+2)               #data type isn't same still python allows addition by handling it internally
print(type(8+2))
'''
INDEXING AND SLICING
'''
ae=np.arange(20)
ae_slice=slice(1,10,2)   #start,stop and step
elm=ae[6]
print(ae[ae_slice])
ae=np.arange(20)
print(ae[2:9])
ae=np.arange(20)
print(ae[2:])
ae=np.arange(20)
print(ae[:9])
ar=np.array([[1,2,3],[21,334,11],[11.1,2.2,33.1]])
print(ar[0:2,0:2])      #slices first two rows and first two columns
print(ar[0:4,0:20])     # it'll work but it's confusing so we shouldn't use it.
print(ar[1:,0:])
print(ar[:2,:1])
'''
NumPy Array attributes
'''
at=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(at.shape)                          #returns a tuple consisting of array dimensions
print(at.ndim)                           #returns the no. of array dimensions
print(at.itemsize)                       #returns the length of each element pof array in bytes
'''
numpy.empty-->creates an uninitialized array of specified shape and data type
'''
ay=np.empty([3,2],dtype=int)
print(ay)
au=np.empty([3,2],dtype=str)
print(au)
ao=np.empty([3,2],dtype=float)
print(ao)
'''
Reading and writing from files using NumPy
NumPy provides the option of importing data files directly into ndarray using the loadtxt function
The savetxt function can be used to write data from an array to a file.
'''
az=np.loadtxt('nump.txt')
np.savetxt('nump2.txt',az)
ax=np.arange(0,20)
np.savetxt('nump3.txt',ax)
ac=np.array([[12,1,2],[11,22,33]])
np.savetxt('nump4.txt',ac)
av=np.loadtxt('nump4.txt')
print(av)
'''
Reading and writing from CSV files
NumPy arrays can be dumped into CSV files using savetxt function and the comma delimiter.
The genfromtxt function can be used tom read data from CSV file into a NumPy array.
'''
np.savetxt('nump5.csv',ac,delimiter=',')
ab= np.genfromtxt('nump5.csv', delimiter=',')
print(ab)
