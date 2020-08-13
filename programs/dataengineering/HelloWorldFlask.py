# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 12:32:20 2020

@author: lenovo
"""


from flask import Flask
print(__name__)
app = Flask(__name__)

@app.route("/")
def hello_world():
   return 'Hello World'

@app.route("/greet")
def greeting():
    return " Welcome to Flask"   

@app.route("/greetcustom/<name>")
def customized_greeting(name):
    message = name + " Welcome to Flask"
    return message    


@app.route("/register")
def register():
    return " Registration"   

 

if __name__ == '__main__':
   app.run(debug=True)