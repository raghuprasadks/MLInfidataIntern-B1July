# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 12:45:52 2020

@author: lenovo
"""


import pandas as pd
income = pd.read_csv("income.csv")
print('income ',income)

#Get columns

print('columns ',income.columns)

print ('first two columns ',income.columns[0:2])

#Data types

print('data types ',income.dtypes)

income['State'].dtypes

#Creating new column

income["dummyyear"] = income.Y2008

print(income["dummyyear"])

income.dummyyear

income.dummyyear = income.dummyyear.astype('float')
income.dummyyear.dtype


income.shape

rows = income.shape[0]
print('rows ',rows)
columns = income.shape[1]
print('columns  ',columns)


income.head(10)

income.tail()

income[0:5]
income.iloc[0:4]



s = pd.Series([1,2,3,1,2], dtype="category")
print('categories ',s)

income.Index.unique()

print ('no of unique' ,income.Index.nunique())

print ('cross tab ',pd.crosstab(income.Index,income.State))

df1 = pd.crosstab(income.Index,income.State)

print('cross tab',df1)

income.Index.value_counts()

income.Index.value_counts(ascending = True) 

income.sample(n = 5)
print('sample ')
income.sample(frac = 0.1)

income["State"]
income.State

#df.loc[row_index , column_index]

income.loc[:,["Index","State","Y2008"]]
income.loc[0:2,["Index","State","Y2008"]]  #Selecting rows with Index label 0 to 2 & columns
income.loc[:,"Index":"Y2008"]  #Selecting consecutive columns
#In the above command both Index and Y2008 are included.
income.iloc[:,0:5]  #Columns from 1 to 5 are included. 6th column not included

import numpy as np

x = pd.DataFrame({"var1" : np.arange(1,20,2)}, index=[9,8,7,6,10, 1, 2, 3, 4, 5])
# 1,3,5,7,9
print(x)

print ('iloc index based ', x.iloc[:3])

print ('loc label based ', x.loc[:3])

data = pd.DataFrame({"A" : ["John","Mary","Julia","Kenny","Henry"], "B" : ["Libra","Capricorn","Aries","Scorpio","Aquarius"]})
data 

data.columns = ['Names','Zodiac Signs']

#Renaming only some of the variables.
data.rename(columns = {"Names":"Cust_Name"},inplace = True) 








