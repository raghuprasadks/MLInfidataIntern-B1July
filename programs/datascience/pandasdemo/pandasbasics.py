# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 16:40:49 2020

@author: lenovo
"""
import pandas as pd

'''
Create a series
'''
s = pd.Series([2,4,6,8,10])
print('Series with default index',s)

s1 = pd.Series([2,4,6,8,10],index=['a','b','c','d','e'])
print('Series with custom index ',s1)
print('Shape of a series ',s1.shape)
#(5,)

cities = pd.Series(['Bengaluru','Chennai','Hyderabad'])
print('Cities ',cities)
print('Shape',cities.shape)
sales = pd.Series([10000.50,20000,600000.0])
print('Series with fraction',sales)

'''
Data frame
'''

data = {'Country': ['Belgium', 'India', 'Brazil'],
'Capital': ['Brussels', 'New Delhi', 'Brasília'],
'Population': [11190846, 1303171035, 207847528]}
print('dictionary ',data)
df = pd.DataFrame(data)
print('Data frame ',df)
print('Data frame :: shape',df.shape)
df1 = pd.DataFrame(data,columns=['Country', 'Capital', 'Population'])
print('Dataframe with custom columns ',df1)
'''
Write to csv
'''
df1.to_csv('sample.csv')
'''
Read from csv
'''
df2 = pd.read_csv('sample.csv')
print('Reading a data frame ',df2)
df3 = pd.read_csv('sample.csv',header=None)
print('Reading a data frame without header',df3)
'''
Read an excel file
'''
dfxl = pd.read_excel('coronadashboard.xlsx')
print('Read excel ',dfxl)
print('reading a sheet')
dfkarnatakash= pd.read_excel('coronadashboard.xlsx','karnataka')
print('karnataka sheet ',dfkarnatakash)


