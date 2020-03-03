# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 08:59:24 2019

@author: Lakshmendra Singh
"""
'''
INTRODUCTION TO PANDAS
Pandas in an open source Python Library providing efficient, easy to use data structures and data analysis tools.
The name pandas is derived from "Panel Data"--an econometrics from multidimensional data.
It is suited for:-
1.Tabular data with heterogeneously typed columns.
2.Ordered and unordered time series data.
3.Arbitrary matrix data with row and columns labels.
4.Any other form of observational/statistical data sets.
NOTE-->The data actually need not to be labelled at all to be placed into a pandas data structure.
'''
'''
Data Structures in Pandas
Pandas provide three data structures:-
DATA STRUCTURE             DIMENSIONS         DESCRIPTION
1. Series                      1              Labeled, homogeneous arrayof immutable size
2. DataFrames                  2              Labeled, heterogeneously typed, size mutable tabular Data Structures
3. Panels                      3              Labeled, size-mutable array               
They are built on top of numpy array.
All the above data structures are value-mutable.
'''
'''
1. SERIES
A Series is a single-dimensional array structure that stores hhomogeneous data i.e., data of single type.
All the elements of a Series are value-mutable and size-immutable
Data--->Can be of multiple types such as ndarray, lists, constants, series, dict etc.
Index-->Indexes must be unique and have the same length as data defaults to np.arrange(n) if no index is passed.
dtype-->Data type of each column; if none mentioned, it will be inferred; automatically.
Copy--->Deep copies data, set to false as default.
DEEP COPY-->Copying as much information about data as possible. Eg. a duplicate driver's license which is as good as the original one.
DEEP COPY-->antonym-->SHALLOW COPY
'''
import pandas
import numpy as np
series=pandas.Series()
import pandas as pd
series2 = pandas.Series()
print(series)
arr=np.array([1,21,-45,1+4j,12**2])
series3=pd.Series(arr)
print(series3)
dict1={'a':12,'b':-12,'c':'ALPHA CENTAURI'}
ser4=pd.Series(dict1)
print(ser4)
ser5=pd.Series([1,-23,11,2**2])
print(ser5[1:3])                         #slicing 
print(ser5[:3])                          #slicing 
print(ser5[1:])                          #slicing 
print(ser5[1:9])                         #slicing 
'''
2. DataFrames
A DataFrame is a 2D data structure in which data is aligned in a tabular fashion consisting of rows and columns.
A DataFrame can be created using the following constructor:-
pandas.DataFrame(data, index, dtype, copy)
Data--->Can be of multiple types such as lists, constants, series, dict etc.
Index-->Row and column labels of the DataFrame; defaults to np.arrange(n) if no index is passed.
dtype-->Data type of each column.
Copy--->Creates a deep copy of the data, setto false as default.
 
'''
list1=[1,13,-45,4**8]
df1=pd.DataFrame(list1)
print(df1)
dict2=[{'a':12,'b':'Kuch bhi','c':3**6}]
df2=pd.DataFrame(dict2)
print(df2)
list2=[{'a':12,'b':'Kuch bhi','c':3**6},{'a':122,'b':'Kuch to','c':2**6},{'a':92,'b':"Life's Good",'c':3**9}]
df3=pd.DataFrame(list2)
print(df3)
list3=[{'a':12,'b':'Kuch bhi','c':3**6},{'a':122,'b':'Kuch to','c':2**6,'d':'Aree Bhai Bhai'},{'a':92,'b':"Life's Good",'c':3**9,}]        #it'll print "NaN" for extra column 'd' 
df4=pd.DataFrame(list3)
print(df4)
list4=[{'a':12,'b':'Kuch bhi','c':3**6,'d':12},{'a':122,'b':'Kuch to','c':2**6}]        #it'll print "NaN" for extra column 'd' 
df5=pd.DataFrame(list4, index=['first','second'])                                       #user defined index for rows        use-->increases readability in output viewing
print(df5)
'''
Creating a DataFrame using pandas.series
'''
list4=[{'a':12,'b':34},{'a':1,'b':45},{'a':123,'b':11,'c':11}]
ser6=pd.Series([12,34,56],index=['maths','apppdev','computers'])
ser7=pd.Series([22,74,96],index=['maths','apppdev','computers'])
tbl=pd.DataFrame({
        'Jim':ser6,
        'Moriarty':ser7})
print(tbl)
'''
DataFrame
Addition and Deletion of columns
A new column can be added to a DataFrame when the data is passed as a Series. 
'''
data={'one':pd.Series([1,34,90], index=['alpha','beta','gamma']),
      'two':pd.Series([12,55*2,99.78,12**2], index=['alpha','beta','gamma','delta']) }
table=pd.DataFrame(data)
print(table)
#table['three']=pd.Series([67,89,90,57,98], index=['alpha','beta','gamma','delta','psy'])              this won't work because there's an extra "psy" which we need to add for both "one" and "two"
table['three']=pd.Series([67,89,90,57], index=['alpha','beta','gamma','delta'])                        #this'll work
print(table)
'''
Column Deletion
DataFrame columns can be deleted using del() function 
'''
del(table['two'])                #deletion
print(table)
temp_ser=table.pop('three')      #removes column "three" from "table" and copies it to "temp_ser"
print(temp_ser)                  #prints the popped column of "table"
print(table)
'''
DataFrame
Addition and Deletion of Rows
Dataframe rows can be selected by passing the row label to the loc() function.
'''
print('\n')
data={'one':pd.Series([1,34,90], index=['alpha','beta','gamma']),
      'two':pd.Series([12,55*2,99.78,12**2], index=['alpha','beta','gamma','delta']) }
table=pd.DataFrame(data)
print(table)
print('\n')
print(table.loc['alpha'])          #returns row with label  i.e. more readable output
print('\n')
print(table.iloc[1])               #returns row indexed 1 i.e. mathematical approach                iloc-->integer location
'''
Appending a row
The append() function can be used to add more rows to the DataFrame.
'''
table['three']=pd.Series([67,89,90,57], index=['alpha','beta','gamma','delta']) 
print('\n')
print(table)
nxtrow=pd.DataFrame([[12,45],[12,22]],columns=['two','three'])
table=table.append(nxtrow)
print('\n')
print(table)
#table[0]='psy'
#print('\n')
#print(table)
'''
drop() function
It is used to drop rows whose labels are provided.
'''
table=table.drop('delta')
print('\n')
print(table)
table=table.drop(1)
print('\n')
print(table)
'''
Importing and Exporting Data using Pandas
Data can be loaded into DataFrames from input data stored in CSV format using read_csv() function

'''
tbl2=pd.read_csv("USArrests.csv")
print(tbl2)
table.to_csv("to_csv.csv")
'''
Loading Excel Sheets into Pandas
Data can be loaded into DataFrames from input data stored in the Excelsheet format using read_excel()

'''
sheet=pd.read_excel("LoadPandas.xlsx")
print(sheet)
table.to_excel("SavePandas.xlsx")







