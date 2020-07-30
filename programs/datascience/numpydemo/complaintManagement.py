# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 16:27:07 2020

@author: lenovo
"""


from tkinter import *
import sqlite3

class complaint():
    def _init_(self,root):
        self.f = Frame(root,height=800, width = 500)
        #self.f.propagate(0)
        self.f.pack()
        
        # labels
        #self.l1 = Label(text='Patient Number')
        self.l2 = Label(text='customername')
        self.l3 = Label(text='mobile')
        self.l4 = Label(text='email')
        self.l5 = Label(text='complainttype')
        self.l6 = Label(text='complaint')
        self.l7 = Label(text='status')
        
        #self.l1.place(x=50,y=100)
        self.l2.place(x=50,y=150)
        self.l3.place(x=50,y=200)
        self.l4.place(x=50,y=250)
        self.l5.place(x=50,y=300)
        self.l6.place(x=50,y=350)
        self.l7.place(x=50,y=400)
        
        #Entry for user name
        
        #self.patientnum = Entry(self.f,width = 25,fg='blue',bg='yellow',font=('Arial',14))
        
        self.customername = Entry(self.f,width = 25,fg='blue',bg='yellow',font=('Arial',14))
        
        self.mobile = Entry(self.f,width = 25,fg='blue',bg='yellow',font=('Arial',14))
        
        self.email = Entry(self.f,width = 25,fg='blue',bg='yellow',font=('Arial',14))
        self.complainttype = Entry(self.f,width = 25,fg='blue',bg='yellow',font=('Arial',14))
        self.complaint = Entry(self.f,width = 25,fg='blue',bg='yellow',font=('Arial',14))
        self.status = Entry(self.f,width = 25,fg='blue',bg='yellow',font=('Arial',14))
        
        
        #self.patientnum.place(x=150,y=100)
        self.customername.place(x=150,y=150)
        self.mobile.place(x=150,y=200)
        self.email.place(x=150,y=250)
        self.complainttype.place(x=150,y=300)
        self.complaint.place(x=150,y=350)
        self.status.place(x=150,y=400)
        self.submit=Button(self.f,text='Save',width = 25,height=2,command=self.queryregister)
        self.submit.place(x=150,y=450)
        
    def queryregister(self):
        #patientnum = self.patientnum.get()
        customername = self.customername.get()
        mobile = self.mobile.get()
        email = self.email.get()
        complainttype = self.complainttype.get()
        complaint = self.complaint.get()
        status = self.status.get()
        connection= sqlite3.connect("complaint.db")
        cur = connection.cursor()
        print('cursor ',cur)
        sql = "insert into complaint(customername,mobile,email,complainttype,complaint,status) values (?,?,?,?,?,?)"
        param = (customername,mobile,email,complainttype,complaint,status)
        cur.execute(sql,param)
        connection.commit()
        self.queryregister = cur.lastrowid
        connection.close()
        '''
        select query
        '''
        cur = connection.cursor()
        sql = "SELECT customername, mobile from complaintstat where customername=? and mobile = ?"
        param = (customername,mobile)        
        
        curset = cur.execute(sql,param)
        records = curset.fetchall()
        
        
        print('after select ',type(records))
        
        if (len (records) > 0):
            sql = "update queryregister set total = total +1 where customername=? and mobile = ?" 
            cur.execute (sql,param)
            connection.commit()
            print('data updated ')
        else:
            sql = "insert into queryregister values (?,?,?,?,?,?)"
            param = (customername,mobile,1,1,0,0)
            cur = connection.cursor()
            cur.execute(sql,param)
            connection.commit()
            print('data inserted')