# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 12:14:26 2019

@author: Lakshmendra Singh
"""

'''
Data Manipulation
using numPy, Pandas, Matplotlib we will analyze, visualize and manipulate large datsets in order to extract valuable informations and insights.
'''
'''
Basic functionalities of Series - Ndim()
Ndim() returns the no. of dimensions of the data structure.
'''
import pandas as pd
import numpy as np
df=pd.Series(np.arange(1,51))
print(df.ndim)
'''
Basic functionalities of Series - Axes()
Axes() returns a list of the axes of the row tables.
'''
df=pd.Series(np.arange(1,51))
print(df.axes)
'''
Values
'''
df=pd.Series(np.arange(1,51))
print(df.values)
'''
Basic functionalities of Series - Head()
Head() returns the first n rows of the data structure.
'''
df=pd.Series(np.arange(1,51))
print(df.head(6))
'''
Basic functionalities of Series - tail()
tail() returns the last n rows of the data structure.
'''
df=pd.Series(np.arange(1,51))
print(df.tail(6))
'''
Basic functionalities of Series - Sum()
Sum() returns the sum of the values for the required axis.
'''
d={'odd':np.arange(1,100,2),
   'even':np.arange(0,100,2)}
print(d['odd'])
print(d['even'])
print(pd.DataFrame(d))
df=pd.DataFrame(d)
print(df.sum())
'''
Basic functionalities of Series - std()
std() returns the standard deviation of the values for the requested axis
'''
d={'odd':np.arange(1,100,2),
   'even':np.arange(0,100,2)}
df=pd.DataFrame(d)
print(df.std())
'''
Iterating a DataFrame--  iteritems()
iteritems() iterates over each column as key, value pair.
'''
df=pd.DataFrame(np.random.rand(5,4),
                columns=('col1','col2','col3','col4'))
for key, value in df.iteritems():
    print(key,value)
'''
iterrows()
'''
for key, value in df.iterrows():
    print(key,value)
'''
itertuples()
It returns an iterator yielding a named tuple for each row
'''
for row in df.itertuples():
    print(row)
    print(type(row))
'''
GroupBy Operation
An Object in pandas can be split into multiple ones.
'''
world_cup={'Team':['West Indies','West Indies','India','Australia','Pakistan','Sri Lanka','Australia','Australia','Australia','India','Australia'],
           'Rank':[7,7,2,1,6,4,1,1,1,2,1],
           'Year':[1975,1979,1983,1987,1992,1996,1999,2003,2007,2011,2015]}
df=pd.DataFrame(world_cup)
print(df)
print(df.groupby('Team').groups)
'''
GroupBy Operation--Multiple Columns
The DataFrame is grouped according to the 'Team' and 'ICC_Rank' columns.
'''
world_cup={'Team':['West Indies','West Indies','India','Australia','Pakistan','Sri Lanka','Australia','Australia','Australia','India','Australia'],
           'Rank':[7,7,2,1,6,4,1,1,1,2,1],
           'Year':[1975,1979,1983,1987,1992,1996,1999,2003,2007,2011,2015]}
df=pd.DataFrame(world_cup)
print(df.groupby(['Team','Rank']).groups)
for name,group in df.groupby('Team'):
    print('--------------------------------------------------------------')
    print(name,group)
    print(type(group))
    print(group.sum)
    print(group['Rank'])
print('--------------------------------------------------------------')
'''
Selecting a group
A single group can be selected using get_group()
'''
world_cup={'Team':['West Indies','West Indies','India','Australia','Pakistan','Sri Lanka','Australia','Australia','Australia','India','Australia'],
           'Rank':[7,7,2,1,6,4,1,1,1,2,1],
           'Year':[1975,1979,1983,1987,1992,1996,1999,2003,2007,2011,2015]}
df=pd.DataFrame(world_cup)
grouped=df.groupby('Team')
print(grouped.get_group('India'))
'''
Aggregations
An aggregated function returns a single aggregated value for each group.
'''
d={'odd':np.arange(1,100,2),'even':np.arange(0,100,2)}
print(d['odd'])
print(d['even'])
df=pd.DataFrame(d)
print(df.groupby('odd').groups)             #group of all numbers labelled 'odd' in the DatFrame
'''
Concatenation
Concatenation is the process of combining two or more data structures.
'''
world_champions={'Team':['India','Australia','West Indies','Pakistan','Sri Lanka'],
                 'ICC_Rank':[2,3,7,8,4],
                 'World_Championship_Year':[2011,2015,1979,1992,1996],
                 'Points':[874,787,753,673,855]}
chokers={'Team':['South Africa','New Zealand','Zimbabwe'],
         'ICC_Rank':[1,5,9],
         'Points':[895,764,656]}
df1=pd.DataFrame(world_champions)
df2=pd.DataFrame(chokers)
print(pd.concat([df1,df2]))
print(df1.append(df2))
print(df2.append(df1))
print(pd.concat([df1,df2],axis=0))                   #go along the x axis
print(pd.concat([df1,df2],axis=1))                   #go along the y axis
'''
Merging and Joining
Merging is pandas operation that performs Database joins on objects.
Merging removes duplication while concatenation doesn't.
'''
world_champions={'Team':['India','Australia','West Indies','Pakistan','Sri Lanka'],
                 'ICC_Rank':[2,3,7,8,4],
                 'World_Championship_Year':[2011,2015,1979,1992,1996],
                 'Points':[874,787,753,673,855]}
match_stats={'Team':['India','Australia','West Indies','Pakistan','Sri Lanka'],
             'World_Cups_played':[11,10,11,9,8],
             'ODIs_played':[733,988,712,679,662]}
df1=pd.DataFrame(world_champions)
df2=pd.DataFrame(match_stats)
print(df1)
print(df2)
print(pd.merge(df1,df2,on='Team'))
'''
Left Join
Left Join merges two objects on the keys from the left object.
'''
world_champions={'Team':['India','Australia','West Indies','Pakistan','Sri Lanka'],
                 'ICC_Rank':[2,3,7,8,4],
                 'World_Championship_Year':[2011,2015,1979,1992,1996],
                 'Points':[874,787,753,673,855]}
chokers={'Team':['South Africa','New Zealand','Zimbabwe'],
         'ICC_Rank':[1,5,9],
         'Points':[895,764,656]}
df1=pd.DataFrame(world_champions)
df2=pd.DataFrame(chokers)
print(pd.merge(df1,df2,on='Team',how='left'))
print(pd.merge(df2,df1,on='Team',how='left'))
'''
Right Join
Right Join Merges two objects on the keys from the right object\.
'''
world_champions={'Team':['India','Australia','West Indies','Pakistan','Sri Lanka'],
                 'ICC_Rank':[2,3,7,8,4],
                 'World_Championship_Year':[2011,2015,1979,1992,1996],
                 'Points':[874,787,753,673,855]}
chokers={'Team':['South Africa','New Zealand','Zimbabwe'],
         'ICC_Rank':[1,5,9],
         'Points':[895,764,656]}
df1=pd.DataFrame(world_champions)
df2=pd.DataFrame(chokers)
print(pd.merge(df1,df2,on='Team',how='right'))
print(pd.merge(df2,df1,on='Team',how='right'))
'''
Outer Join
Outer Join merges two objects based on a full union of the columns of both the objects.
'''
world_champions={'Team':['India','Australia','West Indies','Pakistan','Sri Lanka'],
                 'ICC_Rank':[2,3,7,8,4],
                 'World_Championship_Year':[2011,2015,1979,1992,1996],
                 'Points':[874,787,753,673,855]}
chokers={'Team':['South Africa','New Zealand','Zimbabwe'],
         'ICC_Rank':[1,5,9],
         'Points':[895,764,656]}
df1=pd.DataFrame(world_champions)
df2=pd.DataFrame(chokers)
print(pd.merge(df1,df2,on='Team',how='outer'))
print(pd.merge(df2,df1,on='Team',how='outer'))
'''
Inner Join
'''
df1=pd.DataFrame({'key':['k1','k2','k3','k4','k5','k6'],
                  'a':['a1','a2','a3','a4','a5','a6'],
                  'b':['b1','b2','b3','b4','b5','b6']})
df2=pd.DataFrame({'key':['k1','k2','k3','k4'],
                  'c':['c1','c2','c3','c4'],
                  'd':['d1','d2','d3','d4']})
print(pd.merge(df1,df2,on='key',how='inner'))
print(pd.merge(df2,df1,on='key',how='inner'))