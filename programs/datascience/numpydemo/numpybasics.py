# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 06:46:25 2020

@author: lenovo
Reference : https://www.guru99.com/numpy-tutorial.html
"""

'''
What is Numpy

What is NumPy?
NumPy is an open source library available in Python that aids in 
mathematical, scientific, engineering, and data science programming. 
NumPy is an incredible library to perform mathematical and statistical operations. 
It works perfectly well for multi-dimensional arrays and matrices multiplication
'''


'''
Why use NumPy?
NumPy is memory efficiency, meaning it can handle the vast amount of data more 
accessible than any other library. Besides, NumPy is very convenient to work with, 
especially for matrix multiplication and reshaping. 
On top of that, NumPy is fast. In fact, TensorFlow and Scikit learn to use 
NumPy array to compute the matrix multiplication in the back end.
'''

'''
Import NumPy and Check Version
'''

import numpy as np
print(np.__version__)


'''
What is Python Numpy Array?

NumPy arrays are a bit like Python lists, but still very much different at the 
same time
'''


'''
Create a NumPy Array from a list
'''

lst = [1,2,3,4,5]
nparray1 = np.array(lst)
print('nparray from list',nparray1)
print('Datatype',type(nparray1))
#<class 'numpy.ndarray'>

nparray2 = np.array([2,4,5,8])
print('nparray from list another way',nparray2)

#Shape of an array
print('shape ',nparray2.shape)


#Datatype of an array
print('Datatype ',nparray2.dtype)


'''
Create a NumPy Array from a Tuple
'''

nparray3 = np.array((2,5,6,7))
print(nparray3)

'''
Mathematical Operations on an Array
'''
print ('Adding 2 to every element ',nparray3+2)

print ('Multiply  3 with every element ',nparray3*3)


#Float array

floatarry= np.array((2.9,3.0,6))
print('float array ',floatarry)
print('Datatype of float array ',floatarry.dtype)


'''
Two dimensional Array
'''

lst2d = [(1,2,3),(4,5,6)]
twodarray = np.array(lst2d)
print('twodarray ',twodarray)
print('2d Shape ',twodarray.shape)

lst3d = [[(1,2,3),(4,5,6)],[(7,8,9),(10,11,12)]]

threedarray = np.array(lst3d)
print('threedarray ',threedarray)
print('3d Shape ',threedarray.shape)

'''
numpy.zeros()

np.zeros() function is used to create a 
matrix full of zeroes. It can be used when 
you initialize the weights during the first 
iteration in TensorFlow and other statistic 
tasks.
'''
zeros = np.zeros([3,3])
print('zeros ',zeros)

'''
Example numpy zero with datatype
'''

np.zeros((2,2), dtype=np.int16)

'''
numpy.ones()

np.ones() function is used to create a 
matrix full of ones. It can be used when 
you initialize the weights during the 
first iteration in TensorFlow and other 
statistic tasks.

'''
ones = np.ones([4,3])
print('ones ',ones)
print('shape ',ones.shape)


ones3d = np.ones([4,3,2])
print('ones3d ',ones3d)
print('shape ',ones3d.shape)

'''
Reshape
'''

e=np.array([(1,2,3),(4,5,6)])
print('Before reshape ',e)
er =e.reshape(3,2)
print('After reshape ',er)

'''
Flatten Data
'''
print(e.flatten())

'''
Stacking

hstack -With hstack you can appened data horizontally.

'''

f=np.array([1,2,3])
g = np.array([4,5,6])
print('horizontal append ',np.hstack((f,g)))

'''
vstack - With vstack you can appened data vertically
'''

print('Vertical Stack ',np.vstack((f,g)))


'''
Generate Random Numbers
'''

'''
To generate random numbers for Gaussian distribution use

numpy.random.normal(loc, scale, size)

Here

Loc: the mean. The center of distribution
scale: standard deviation.
Size: number of returns

'''

## Generate random nmber from normal distribution
normal_array = np.random.normal(5, 0.5, 10)
print(normal_array)


'''
Matrix is immutable. 
'''

A = np.matrix(np.ones((4,4)))

print('Matrix ',A)

np.array(A)[2]=2

print('Matrix: after updation ',A)

np.asarray(A)[2]=2
print('With asarray ',A)


'''
range in list
'''

for i in range (2,20):
    print(i)
    
    
    
'''
numpy.arange() is an inbuilt numpy function that 
returns an ndarray object containing evenly spaced 
values within a defined interval
'''

np.arange(1, 11)

np.arange(2,20,2)

'''
Linspace gives evenly spaced samples.
numpy.linspace(start, stop, num, endpoint)
'''

np.linspace(1.0, 5.0, num=10)

np.linspace(1.0, 5.0, num=10,endpoint = False)

'''
LogSpace
LogSpace returns even spaced numbers on a log scale. Logspace has the same parameters as np.linspace.
'''

np.logspace(3.0, 4.0, num=4)

'''
Indexing and slicing
'''	

e  = np.array([(1,2,3), (4,5,6)])
print(e)

print('0th row ',e[0])
print('1st row',e[1])
print('0th column ',e[:,0])

print('1st row two columns ',e[1, :2])


'''
Statistical function
Numpy is equipped with the robust statistical function
'''

normal_array = np.random.normal(5, 0.5, 10)
print(normal_array)	

### Min 
print(np.min(normal_array))

### Max 
print(np.max(normal_array))

### Mean 
print(np.mean(normal_array))

### Median
print(np.median(normal_array))

### Sd
print(np.std(normal_array))

'''
Numpy.dot product
'''

## Linear algebra
### Dot product: product of two arrays
f = np.array([1,2])
g = np.array([4,5])
### 1*4+2*5
np.dot(f, g)

'''
Matrix multiplication
'''

### Matmul: matruc product of two arrays
h = [[1,2],[3,4]] 
i = [[5,6],[7,8]] 
### 1*5+2*7 = 19
np.matmul(h, i)

