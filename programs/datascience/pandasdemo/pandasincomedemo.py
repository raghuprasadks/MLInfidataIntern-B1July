# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 12:45:52 2020

@author: lenovo
https://www.listendata.com/2017/12/python-pandas-tutorial.html
"""


import pandas as pd
income = pd.read_csv("income.csv")
print('income ',income)

print ('type ',type(income))

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

income.head()
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

data2 = data.rename(columns = {"Names":"Cust_Name"})
print(data2)
#Renaming only some of the variables.
data.rename(columns = {"Names":"Cust_Name"},inplace = True) 

income.set_index("Index",inplace = True)
income.head()

income.drop('Index',axis = 1)

income1  = income.drop('State',axis=1)

income2 = income1.drop([4,5,6,7],axis=0)
print(income2)

income.sort_values("State",ascending = True)

income["difference"] = income.Y2008-income.Y2009
print(income["difference"])

data = income.assign(ratio = (income.Y2008 / income.Y2009))
data.head()

stat = income.describe()

income.mean()

income.agg(["mean","median"])

income.loc[:,["Y2002","Y2008"]].max()

income.groupby("Index")["Y2002","Y2003"].agg(["min","max","mean"])

income[income.Index == "A"]

income[income.State == "Alabama"]

income.Index == "A"

income.loc[income.Index == "A","State"]

income.loc[(income.Index == "A") & (income.Y2002 > 1500000),:]

income.query('Y2002>1700000 & Y2003 > 1500000')


crops.isnull() 
crops.notnull()  #opposite of previous command.
crops.isnull().sum()  #No. of missing values.

income[income.Index == "A"]

income.loc[income.Index == "A",:]

income.loc[income.Index == "A","State"]

income.loc[(income.Index == "A") & (income.Y2002 > 1500000),:]

income.loc[(income.Index == "A") | (income.Index == "W"),:]

#Alternatively.
income.loc[income.Index.isin(["A","W"]),:]

income.query('Y2002>1700000 & Y2003 > 1500000')


import numpy as np
mydata = {'Crop': ['Rice', 'Wheat', 'Barley', 'Maize'],
        'Yield': [1010, 1025.2, 1404.2, 1251.7],
        'cost' : [102, np.nan, 20, 68]}
crops = pd.DataFrame(mydata)
crops

crops.isnull()

crops.dropna(subset = ['Yield',"cost"],how = 'any').shape

crops['cost'].fillna(value = "UNKNOWN",inplace = True)
crops


data = pd.DataFrame({"Items" : ["TV","Washing Machine","Mobile","TV","TV","Washing Machine"], "Price" : [10000,50000,20000,10000,10000,40000]})
data


data.loc[data.duplicated(),:]

data.loc[data.duplicated(keep = "first"),:]

data.drop_duplicates(keep = "first")


'''
iris dataset
'''

iris = pd.read_csv("iris.csv")

print(iris)

iris.head()

iris["setosa"] = iris.Species.map({"setosa" : 1,"versicolor":0, "virginica" : 0})
iris.head()

dummiers = pd.get_dummies(iris.Species,prefix = "Species")

species_dummies = pd.get_dummies(iris.Species,prefix = "Species").iloc[:,0:]


iris = pd.concat([iris,species_dummies],axis = 1)
iris.head()

income.mean()

income.agg(["mean","median"])





