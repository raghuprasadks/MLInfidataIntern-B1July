# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 14:00:48 2020

@author: lenovo
"""

class Corona():
    '''
    Instance varible
    '''
    state=''
    totalcases=0
    cured=0
    active=0
    died=0
    
    '''
    method
    '''
    def addCases(self,state,totalcases,cured,active,died):
        self.state = state
        self.totalcases = totalcases
        self.cured = cured
        self.active = active
        self.died = died
    
    def info(self):
        return "Info : State ",self.state," total cases",self.totalcases

'''
Object 1 - karnataka
'''
karnataka = Corona()
karnataka.addCases('Karnataka',4000,2000,1500,500)
print('karnataka case info ',karnataka.info())

'''
Object 2 - tn
'''

tn = Corona()
tn.addCases('Tamil Nadu',5000,3000,1500,500)
print('Tamil Nadu case info ',tn.info())


'''
Constructor
Java - C++

class Vehicle{
//Constructor
public Vehicle(String manu,String model,double price){
}

}

__init__

108 Dosa's

batter,ghee,masala
batter,ghee,plain
batter,ghee,masala,cheese

method overloading

name,address,mobile,email,proof

'''

import random
class Account():
    '''
    constructor
    '''
    def __init__(self,name,address,mobile,email,idproof,aadhar=None):
        
        self.name = name
        self.address= address
        self.mobile = mobile
        self.email = email
        self.idproof=idproof
        if (aadhar):
            self.aadhar = aadhar
        
        self.acctno = int(random.random()*1000)
        self.balance = 0
        
    def deposit(self,acctno,amount):
        self.balance = self.balance + amount
        return self.balance
    
    def withdraw(self,acctno,amount):
        self.balance = self.balance - amount
        return self.balance
        
    def checkBalance(self,acctno):
        return self.balance
        
    def info(self):
        return "Name - ",self.name ," Balance - ",self.balance

acctList = []
myact = Account("raghu","Bengaluru",9845547471,'prasadraghuks@gmail.com',2020202020)
print('account no ',myact.acctno)

acctno = myact.acctno
balance = myact.deposit(acctno,10000)
print("Balance after initial deposit ",balance)
balance = myact.deposit(acctno,15000)
print("Balance after second deposit ",balance)
balance = myact.withdraw(acctno,5000)
print("Balance after first withdraw ",balance)
balance = myact.checkBalance(acctno)
print("Check Balance:: ",balance)

acctList.append(myact)

sureshact = Account("Suresh","Bengaluru",9845547472,'sureshraghuks@gmail.com','Property agreement',3999999999)
print('account no ',sureshact.acctno)  
acctno = sureshact.acctno
balance = sureshact.deposit(acctno,50000)
acctList.append(sureshact)

total = 0
for act in acctList:
    print('Info ' ,act.info())
    total = total + act.balance
    
print('total ',total)
  

class product():
    
    def __init__(self,code,name,manufacturer,price):
        self.code = code
        self.name = name
        self.manufacturer = manufacturer
        self.price = price
        
    def info(self):
        print("Code ",self.code," Name ", self.name," manufacturer ",self.manufacturer," price ",self.price)
        
total = 0
productList = []

prod1 = product(123,"Xiaomi Phone","Xiaomi",16000)
maximum = prod1.price
minimum = prod1.price
productList.append(prod1)

prod2 = product(456,"HP Laptop","HP",75000)
productList.append(prod2)

prod3 = product(789,"Sony TV","Sony",60000)
productList.append(prod3)

for pro in productList:
    pro.info()
    total = total + pro.price
    if(pro.price >= maximum):
        maximum = pro.price
    if(pro.price <= minimum):
        minimum = pro.price

print("total ",total)
print("maximum price ",maximum)
print("minimum price ",minimum)

