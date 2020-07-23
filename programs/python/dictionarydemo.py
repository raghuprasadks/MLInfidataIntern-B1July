# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 13:22:10 2020

@author: lenovo
"""

'''
dictionary Key Value pair
index - slicing
no duplicate values
'''

'''
dictionary creation
'''
phonedict={}
'''
Assigning values
'''
phonedict['raghu']=9845547471
phonedict['ramya']=9845547472
phonedict['rashan']=9845547473
print(phonedict)
#{'raghu': 9845547471, 'ramya': 9845547472, 'rashan': 9845547473}
phonedict.update({'raghu': 9845547479})
print('updated ' ,phonedict)

print('keys ' ,phonedict.keys())
print('values ' ,phonedict.values())

del phonedict['raghu']
for k,v in phonedict.items():
    print('key ',k,' value ',v)
    
'''
eval
'''

lst1 = eval(input("Enter a list"))
print(lst1)

coronalist=[]
noofstate=int(input("Enter number of states"))

for n in range(noofstate):
    statedict={}
    name = input("Enter state name")
    lst = eval(input("Enter state data as a list"))
    statedict[name]=lst
    coronalist.append(statedict)
    
print("Corona dashboard using dictionary and list ",coronalist)

'''
[{'Karnataka': [4000, 2000, 1800, 200]}, {'Tamil Nadu': [5000, 3000, 1500, 500]}]
'''

lst = [10,'',25,30]
print(lst)
    




