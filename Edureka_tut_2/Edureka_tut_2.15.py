# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 11:48:08 2019

@author: Lakshmendra Singh
"""
'''
Matplot library
Python provides matplot library for plotting and visualisation.
Matplot library is specially designed for the developement of graphs, charts etc., in order to provide interactive data visualization.
Matplot library is inspired from MATLAB software and reproduces many of its features.

'''
import matplotlib.pyplot as plt
import numpy as np
plt.plot([1,2,3,4])
plt.show()
plt.plot([0,1,2,3,4])           # y values are given x values are implicit
plt.show()
plt.plot([1,2,-2,11])
plt.show()
y_val=[0,1,2,3,4,5]
print([i**2 for i in y_val])
plt.plot(y_val,[i**2 for i in y_val])
plt.show()
plt.grid(True)
plt.plot(y_val,[i**2 for i in y_val])
plt.show()
x=np.arange(0,5,0.1)
plt.plot(x,[i**2 for i in x])
plt.show()
'''
Multiline Plots
Multiple functions can be drawn on the same plot.
'''
x1=range(5)
plt.plot(x1,[x2 for x2 in x1])
plt.plot(x1,[x2*x2 for x2 in x1] )
plt.plot(x1,[x2*x2*x2 for x2 in x1])
plt.grid(True)
plt.show()
x1=range(5)
plt.plot(x1,[x2**2 for x2 in x1])
plt.plot(x1,[x2**10 for x2 in x1] )
plt.grid(True)
plt.show()
x1=range(5)
plt.plot(x1,[x2 for x2 in x1],x1,[x2*x2 for x2 in x1],x1,[x2*x2*x2 for x2 in x1])            #multiple curve plotting using single statement
plt.grid(True)
plt.show()
'''
Limit the Axes
The scale of the plot can be set using axis()
'''
x1=range(5)
plt.plot(x1,[x2 for x2 in x1],x1,[x2*x2 for x2 in x1],x1,[x2*x2*x2 for x2 in x1])            #multiple curve plotting using single statement
plt.grid(True)
plt.axis([-1,5,-1,100])                                                                      #limiting the plot to a certain area
plt.show()
x1=range(5)
plt.plot(x1,[x2 for x2 in x1],x1,[x2*x2 for x2 in x1],x1,[x2*x2*x2 for x2 in x1])            #multiple curve plotting using single statement
plt.grid(True)
plt.axis([1,50,0,100])                                                                       #limiting the plot to a certain area
plt.show()
x1=range(5)
plt.plot(x1,[x2 for x2 in x1],x1,[x2*x2 for x2 in x1],x1,[x2*x2*x2 for x2 in x1])            #multiple curve plotting using single statement
plt.xlim(-1,21)                                                                              #an alternative way of limiting        -->this way is more preffered
plt.ylim(0,61)                                                                               #an alternative way of limiting        -->this way is more preffered
plt.grid(True)
plt.show()
'''
Adding Labels
'''
x1=range(5)
plt.plot(x1,[x2 for x2 in x1],x1,[x2*x2 for x2 in x1],x1,[x2*x2*x2 for x2 in x1])            #multiple curve plotting using single statement
plt.grid(True)
plt.xlabel('X-axis')                                                                         #label
plt.ylabel('Y-axis')                                                                         #label
plt.show()
'''
Adding the Title
'''
x1=range(5)
plt.plot(x1,[x2 for x2 in x1],x1,[x2*x2 for x2 in x1],x1,[x2*x2*x2 for x2 in x1])            #multiple curve plotting using single statement
plt.grid(True)
plt.xlabel('X-axis')                                                                         #label
plt.ylabel('Y-axis')                                                                         #label
plt.title('Learning matplotlib')                                                             #title                         
plt.show()
'''
Adding a Legend
Legends explain the meaning of each line in the graph.
'''
x1=range(5)
plt.plot(x1,[x2 for x2 in x1],label='Linear')
plt.plot(x1,[x2*x2 for x2 in x1],label='Quadratic' )
plt.plot(x1,[x2*x2*x2 for x2 in x1],label='Cubic')
plt.grid(True)
plt.xlabel('X-axis')                                                                         #label
plt.ylabel('Y-axis')                                                                         #label
plt.title('Learning matplotlib')                                                             #title    
plt.legend()                                                                                 #legend to show what is the meaning/label of each line                                                                            
plt.show()
'''
Saving Plots
'''
x1=range(5)
plt.plot(x1,[x2 for x2 in x1],label='Linear')
plt.plot(x1,[x2*x2 for x2 in x1],label='Quadratic' )
plt.plot(x1,[x2*x2*x2 for x2 in x1],label='Cubic')
plt.grid(True)
plt.xlabel('X-axis')                                                                         #label
plt.ylabel('Y-axis')                                                                         #label
plt.title('Learning matplotlib')                                                             #title    
plt.legend() 
plt.savefig('plot.png')                                                                      #legend to show what is the meaning/label of each line                                                                            
plt.show()
'''
Plot types
1. Scatter Plot
2. Histogram
3. Bar Graph
4. Pie Chart
'''
'''
1. Histogram
It shows a distribution of a varible over a range of frequencies or values.
'''
print(np.random.randn(12,4))
y=np.random.randn(100,100)
plt.hist(y)
plt.grid(True)
plt.show()
y=np.random.randn(10,10)
plt.hist(y,100)
plt.grid(True)
plt.show()
'''
Bar Chart
'''
plt.bar([1,23,43,9],[92,45,78,11])
plt.grid(True)
plt.show()
d={'a':1,'b':23,'c':34,'d':45}
for i,key in enumerate(d):
    print(i,key)
    plt.bar(i, d[key])
plt.show()
d={'a':1,'b':23,'c':34,'d':45}
for i,key in enumerate(d):
    plt.bar(i, d[key])
plt.xticks(np.arange(len(d)),d.keys())
plt.show()
'''
Pie Chart
Pie Charts are used to compare multiple parts against the whole.
'''
plt.figure(figsize=(3,3))
x=[12,39,59]
labels=['Las Venturas','San Fierro','Los Santos']
plt.pie(x,labels=labels)
plt.show()
plt.figure(figsize=(4,4))
plt.pie([12,67,1,98],labels=['Shazam','Aquaman','Superman','Batmam'])
plt.show()
'''
Scatter Plot
Scatter plots display values for two sets of data, visualised as a collection of points.
'''
x=np.random.rand(1000)
y=np.random.rand(1000)
plt.scatter(x,y)
plt.show()
x=np.random.randn(20)
y=np.random.randn(20)
plt.scatter(x,y)                           #x and y must have the same size             
plt.show()
'''
Styling
Matplot allows you to choose custom colors for plots. 
'''
y=np.arange(1,3)
plt.plot(y,'Y')                        #second parameter is specifying the color of the curve
plt.plot(y+5,'m')
plt.plot(y+10,'c')
plt.show()
'''
Color Codes
b-->blue
c-->cyan
g-->green
k-->black
m-->magenta
r-->red
w-->white
y-->yellow
'''    
'''
Styling a line in a particular pattern.
'''
y=np.arange(1,100)
plt.plot(y,'--',y*5,'-.',y*10,':',y*15,'-')               #you can't give color and line styling at same time
plt.show()
'''
Control marker styling
Matplot lib provides customization options for markers.
'''
y=np.arange(1,3,0.2)
plt.plot(y,'*',y+0.5,'o',y+1,'D',y+2,'^',y+3,'s')             #*-->Star, o-->Circle, D-->Diamond, ^-->Triangle, s--> Square
plt.show()