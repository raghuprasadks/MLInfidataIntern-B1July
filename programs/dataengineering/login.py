# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 13:30:56 2020

@author: lenovo
"""


from flask import Flask, redirect, url_for, request
app = Flask(__name__)
@app.route('/success/<name>')
def success(name):
   return 'welcome %s' % name
@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['nm']
      return user
      #return redirect(url_for('success',name = user))
   else:
      user = request.args.get('nm')
      return user
      #return redirect(url_for('success',name = user))
if __name__ == '__main__':
   app.run(debug = True)