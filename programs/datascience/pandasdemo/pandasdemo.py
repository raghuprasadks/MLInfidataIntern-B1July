# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 16:26:03 2020

@author: lenovo
"""

import pandas as pd

'''
1 - Series - One dimensional Array
'''
even=pd.Series([2,4,6,8,10])
print('Series')
print(even)
print('data type ',type(even))
'''
index data
0     2
1     4
2     6
3     8
4    10
dtype: int64
'pandas.core.series.Series'>
'''
income=pd.Series([20000,499999,69999,89999,10000],index=['a','b','c','d','e'])
print('income ',income)

testseries=pd.Series((1,2,4,6,8,10))
print('test series' ,testseries)

print('Shape of series ',testseries.shape)

'''
2 - Pandas  - Two dimensional Array
'''

data = {'Country':["India","China","Japan"],'Capital':["Delhi","Beijing","Tokio"],'Population':[7,30,5]}
print('data ',data)    
df = pd.DataFrame(data)

print('Data frame ',df)             
print('Data frame shape',df.shape) 
print('Data frame columns',df.columns) 
print('Data frame country ',df.Country) 
print('Data frame Capital ',df.Capital) 
print('To dataframe to a csv')
df.to_csv('data.csv')






            

        
                   
                   





