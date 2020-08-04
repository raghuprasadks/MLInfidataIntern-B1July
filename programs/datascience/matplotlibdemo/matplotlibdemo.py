# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 11:11:55 2020

@author: lenovo
"""


'''
Matplotlib Demo
1. Basic Line Chart
'''

import numpy as np
import matplotlib.pyplot as pl

x=np.linspace(1,5,6)
print('x value ',x)

y=np.log(x)
print('y value',y)
pl.plot(x,y)
pl.show()

'''
2. Line chart with list as input
'''

a=[1,2,3,4]
b=[2,4,6,8]
c=[1,4,9,16]
pl.title('Demo of line chart')
pl.xlabel("Some Values")
pl.ylabel("Double values")
pl.plot(a,b)

pl.xlabel("Some Values")
pl.ylabel("Squared values")
pl.plot(a,c)

'''
3. Changing Line Style,Line Width and Line Color in a 
Line Chart
'''

x=np.arange(0.,10,0.1)
a=np.cos(x)
b=np.sin(x)
pl.plot(x,a,'b')
pl.plot(x,b,'r')
pl.show()

'''
Change line width
'''
pl.plot(x,a,'b',linewidth=2)
pl.plot(x,b,'r',linewidth=4)
pl.show()


'''
Change line style,width
'''
pl.plot(x,a,'b',linewidth=2,linestyle="dashed")
pl.plot(x,b,'r',linewidth=4,linestyle="dotted")
pl.show()


'''
Marker type,Size and Color
'''
p=[1,2,3,4]
q=[2,4,6,8]
pl.plot(p,q,'k',marker='d',markersize=5,markeredgecolor='red')
pl.show()
#Line Color and marker style combined so marker takes same
#color as line
pl.plot(p,q,'r+',linestyle='solid')
pl.show()

#Marker color separately
pl.plot(p,q,'r+',linestyle='solid',markeredgecolor='b') 
pl.show()

#Without line style
pl.plot(p,q,'ro')
pl.show()


'''
2. Bar Chart
'''
a,b,c=[1,2,3,4],[2,4,6,8],[1,4,9,16]

pl.bar(a,b)
pl.bar(a,c)

#labels
pl.bar(a,b)
pl.xlabel('Values')
pl.ylabel('Doubles')

'''
cities and population
'''
cities=['Delhi','Mumbai','Bangalore','Hyderabad']
population=[10000000,30000000,15000000,20000000]
pl.bar(cities,population)
pl.xlabel('Cities')
pl.ylabel('Population')
pl.show()

pl.bar(cities,population,width=1/2)
pl.show()
pl.bar(cities,population,width=[0.5,0.6,0.7,.8])
pl.bar(cities,population,color=['red','b','g','black'])
pl.show()

'''
Multiple Bar charts
'''
A = [2,4,6,8]
B=[2.8,3.5,6.5,7.7]
X=np.arange(len(A))
#X=range(4)
print(X)
print(type (X))

print(X)
pl.bar(X,A,color='red',width=0.35)
pl.bar(X+0.35,B,color='blue',width=0.35)
pl.show()

'''
Customizing the plot
Anatomy of a chart
'''
'''
Adding Title,Setting X and Y labels,Limits and Ticks
'''
'''
without limit
'''
import numpy as np
import matplotlib.pyplot as plt
plt.title("A Bar Chart")
X=np.arange(4)
print(X)

Y=[5,25,45,20]
#plt.xlim(-2.0,4.0)
plt.bar(X,Y)
plt.show()


import numpy as np
import matplotlib.pyplot as plt
plt.title("A Bar Chart")
X=np.arange(4)
Y=[5,25,45,20]
plt.xlim(-2.0,4.0)
plt.bar(X,Y)
plt.show()

'''
ticks
'''
q=range(4)
s=[23.5,25,26,28.5]
plt.xticks([0,1,2,3])
plt.bar(q,s,width=0.25)
plt.show()

q=range(4)
s=[23.5,25,26,28.5]
plt.xticks([0,0.5,1,1.5,2,2.5,3])
plt.bar(q,s,width=0.25)
plt.show()

'''
Volunteering week 
A-F
Mon-Saturday
a. Create a bar chart showing the collection amount
'''

col=[8000,12000,9800,11200,15500,7300]
X=np.arange(6)
plt.title("Volunteering Week Collection")
plt.bar(X,col,color='r',width=0.25)
plt.show()

'''
b. Plot the collected amount vs days using a bar chart
'''
plt.title("Volunteering Week Collection")

plt.bar(X,col,color='olive',width=0.25)
plt.xticks(X,['Mon','Tue','Wed','Thu','Fri','Sat'])
plt.show()

'''
c. Plot the collected amount vs sections using a bar chart
'''

plt.bar(X,col,color='g',width=0.25)
plt.xticks(X,['A','B','C','D','E','F'])
plt.show()

'''
Adding legends
'''

import numpy as np
import matplotlib.pyplot as plt
Value =[[10,20,30,40],[20,40,60,80],[30,60,120,160],[50,100,150,200]]
X=np.arange(4)

plt.bar(X+0.00,Value[0],color='b',width=0.25,label='Confirmed')
plt.bar(X+0.25,Value[1],color='g',width=0.25,label='Active')
plt.bar(X+0.50,Value[2],color='y',width=0.25,label='Recovered')
plt.bar(X+0.75,Value[3],color='r',width=0.25,label='Dead')
plt.legend(loc='upper left')
plt.title('Corona Dashboard')
plt.xlabel('Statewise Cases')
plt.ylabel('Numbers')
plt.show()


'''
Multiple line charts on common plot where three data ranges are plotted 
on same chart
'''

import numpy as np
import matplotlib.pyplot as plt
Value =[[5,25,45,20],[8,13,29,27],[9,29,27,39]]
X=np.arange(4)
plt.plot(X,Value[0],color='b',label='range1')
plt.plot(X,Value[1],color='g',label='range2')
plt.plot(X,Value[2],color='r',label='range3')
#plt.bar(X+0.75,Value[3],color='r',width=0.25,label='Dead')
plt.legend(loc='upper left')
plt.title('MultiRange Line Chart')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()

'''
Saving a figure
'''
#plt.savefig("multiline-new.png")
plt.savefig('foo1.pdf', bbox_inches='tight')

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.plot([1,2,3])
plt.savefig('myfig.png')


'''
Matplotlib object oriented interface
https://www.tutorialspoint.com/matplotlib/matplotlib_axes_class.htm
'''

'''
Following example shows the advertisement expenses and 
sales figures of TV and 
smartphone in the form of line plots.
'''

import matplotlib.pyplot as plt
y = [1, 4, 9, 16, 25,36,49, 64]
x1 = [1, 16, 30, 42,55, 68, 77,88]
x2 = [1,6,12,18,28, 40, 52, 65]
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
l1 = ax.plot(x1,y,'ys-') # solid line with yellow colour and square marker
l2 = ax.plot(x2,y,'go--') # dash line with green colour and circle marker
ax.legend(labels = ('tv', 'Smartphone'), loc = 'lower right') # legend placed at lower right
ax.set_title("Advertisement effect on sales")
ax.set_xlabel('medium')
ax.set_ylabel('sales')
plt.show()

'''
Subplots
'''

x=np.linspace(0,5,11)
y= x**2
fig,axes=plt.subplots(nrows=1,ncols=2)
'''
for caxes in axes:
    caxes.plot(x,y)
''' 
axes[0].plot(x,y)
axes[1].plot(y,x)
axes[0].set_xlabel('xlabel')
axes[0].set_ylabel('ylabel')
axes[1].set_xlabel('x1 label')
axes[1].set_ylabel('y 1label')

axes[0].set_title('Title 1')
axes[1].set_title('Title 1')


'''
Scatter plot
'''

import matplotlib.pyplot as plt
girls_grades = [89, 90, 70, 89, 100, 80, 90, 100, 80, 34]
boys_grades = [30, 29, 49, 48, 100, 48, 38, 45, 20, 30]
grades_range = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
fig=plt.figure()
ax=fig.add_axes([0,0,1,1])
ax.scatter(grades_range, girls_grades, color='r')
ax.scatter(grades_range, boys_grades, color='b')
ax.set_xlabel('Grades Range')
ax.set_ylabel('Grades Scored')
ax.set_title('scatter plot')
plt.show()

'''
grids
'''

import matplotlib.pyplot as plt
import numpy as np
fig, axes = plt.subplots(1,3, figsize = (12,4))
x = np.arange(1,11)
axes[0].plot(x, x**3, 'g',lw=2)
axes[0].grid(True)
axes[0].set_title('default grid')
axes[1].plot(x, np.exp(x), 'r')
axes[1].grid(color='b', ls = '-.', lw = 0.25)
axes[1].set_title('custom grid')
axes[2].plot(x,x)
axes[2].set_title('no grid')
fig.tight_layout()
plt.show()


'''
Subplots to grid
'''

import matplotlib.pyplot as plt
a1 = plt.subplot2grid((3,3),(0,0),colspan = 2)
a2 = plt.subplot2grid((3,3),(0,2), rowspan = 3)
a3 = plt.subplot2grid((3,3),(1,0),rowspan = 2, colspan = 2)
import numpy as np
x = np.arange(1,10)
a2.plot(x, x*x)
a2.set_title('square')
a1.plot(x, np.exp(x))
a1.set_title('exp')
a3.plot(x, np.log(x))
a3.set_title('log')
plt.tight_layout()
plt.show()