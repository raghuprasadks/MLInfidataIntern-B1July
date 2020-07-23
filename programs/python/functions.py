# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 13:43:11 2020

@author: lenovo
"""
def greet():
    print('Hello.Welcome to ML/DS internship')

greet()

def greet(name):
    print(name, 'Welcome to ML/DS internship')

greet("ravi")

name = input("Enter your name")
greet(name)

def SimpleInterest(p,r,t):
    return (p*r*t)/100

p= int(input("Enter principal"))
r = float(input("Enter the rate of interest"))
t = int(input("Enter the time"))

si = SimpleInterest(p,r,t)
print('simple interest ',si)    



