# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 05:34:53 2020

@author: lenovo
Reference
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.loc.html
"""


import pandas as pd
# 1. Read data from result.xlsx and display records
result = pd.read_excel("result.xlsx")
print('Records')
print(result)

# 2. Display shape

print('shape')
datashape = result.shape
print(datashape)

# 3. Display columns
print('columns')
print(result.columns)

# 4. Display first three columns

print('first three columns')
print(result.columns[0:3])

# 4. Display columns sub1,sub2,sub3

print('Display sub1,sub2,sub3')
print(result.columns[5:8])

# 5. Display first two records from the beginning

print('Display first two records')
print(result.head(2))

#display one record
firstrecord =result.loc[0]
print(firstrecord)
print(type(firstrecord))

#display two record
tworecords =result.loc[[0,1]]
print(tworecords)
print(type(tworecords))

#display two records. Show only name,college,branch

reccolumns = result.loc[[0,1],'name']
print(reccolumns)

reccolumns = result.loc[[0,1],'name':'sub3']
print(reccolumns)

reccolumns = result.loc[[0,1],['name','sub3']]
print(reccolumns)

reccolumns = result.loc[:,['name','sub3']]
print(reccolumns)


#using iloc
displayall = result.iloc[:,:]
print(displayall)

#using iloc
displayall = result.iloc[[0,1],:]
print(displayall)
print('data type ',type(displayall))

displayall = result.iloc[[0,1],[0,6]]
print(displayall)
print('data type ',type(displayall))


displayall = result.iloc[[0,1],0:6]
print(displayall)
print('data type ',type(displayall))

# 6. Display of filtered data

#display raghu's record
result.loc[result['name']=='raghu',['name','college','branch']]

