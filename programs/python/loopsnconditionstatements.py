# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 13:26:50 2020

@author: lenovo
"""
'''
loops in python

while loop
'''

start = 1
end = 10

while (start <=end):
    print(start)
    start = start + 1

'''
for loop
'''

for i in range (1,11):
    print(i)

for i in range (2,21,2):
    print(i)
    
students=['ravi','rashmi','gagan']

for s in students:
    print(s)    


age = 17
if (age <18):
    print('you are not elibible to vote')
else:
    print('you are eligible to vote')

marks = 80
if (marks >90 and marks <=100):
    print('A+')
elif (marks >80 and marks <=90):
    print('A')
elif (marks >70 and marks <=80):
    print('B+')
else:
    print('Other grade')
    
    
    






