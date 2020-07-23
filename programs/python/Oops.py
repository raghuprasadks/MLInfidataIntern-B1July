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


        
