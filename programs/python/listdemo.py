# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 13:53:07 2020

@author: lenovo
"""

'''
CRUD - Create, Read,Update and Delete
Create
'''
data = [30,40,50,60]
print('original list ',data)
data.append(70)
print('After append ',data)
'''
Read
'''
for d in data:
    print(d)

'''
update
'''
data[1]=42
print('after update',data)
'''
delete
'''
del data[0]
print('after delete',data)
data1 = [30,40,50,60,70,80,90,100]
print(data1[0:3])
data2 = data1[0:3]
print('slicing ',data2)

'''
length of list
'''
length = len (data2)
print(length)
maximum = max(data1)
print('maximum ',maximum)
minimum = min(data1)
print('minimum ',minimum)
total = sum(data1)
print('sum ',total)


'''
Dynamically create a list of marks
'''
sub = int(input("Enter no of subjects"))

markslist=[]

for i in range(sub):
    marks = int(input("Enter marks"))
    markslist.append(marks)
    
print('marks list',markslist)


coronadash = []
col = int(input("Enter the number of columns in the corona dashboard"))
headerlist=[]
for i in range(col):
    val= input("Enter the header name")
    headerlist.append(val)
coronadash.append(headerlist)
print('header',headerlist)
print('dashboard',coronadash)


'''
Harshita
'''


coronadash = []
headerlist = []
state = []
col = int(input("Enter the number of columns in the corona dashboard"))

for i in range(col):
    headerlist.append(input("Enter the header name"))
coronadash.append(headerlist)

states = int(input("Enter the number of states"))

for i in range(states):
    state=[]
    for j in range(col):
        state.append(input("Enter data"))
    
    coronadash.append(state)

print(coronadash)  

'''
[['state', 'total', 'cured', 'active', 'died'], 
 ['karnataka', '4000', '2000', '1800', '200']
 ['Tamil Nadu', '5000', '3000', '1500', '500']] 
'''


'''
Ananth
'''

state=int(input('Enter the number of states'))
coronadashboard=[]

for i in range(state):
    statename=input('enter the name of state')
    statena=[]
    statena.append(statename)
    totalcase=int(input('enter the total cases'))
    totalca=[]
    totalca.append(totalcase)
    curedcase=int(input('enter the cured cases'))
    curedca=[]
    curedca.append(curedcase)
    activecase=int(input('enter the active case'))
    activeca=[]
    activeca.append(activecase)
    deadcase=int(input('enter deadcase'))    
    deadca=[]
    deadca.append(activecase)
   
    coronadashboard.append(statena)
    coronadashboard.append(totalca)
    coronadashboard.append(curedca)
    coronadashboard.append(deadca)

print(coronadashboard)


'''
total 

    





