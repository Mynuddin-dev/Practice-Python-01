# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 06:12:08 2020

@author: Mynuddin
"""
class Computer:
    def config(self):
        print("It's Corei5, 8GB Ram, 1TB HDD")
        

"""x=9  #x is an object of integer
print(type(x))
y="Name"
print(type(y))
print(type(comp1))"""

comp1=Computer()    #its our object we creat
comp2=Computer()

Computer.config(comp1)
Computer.config(comp2)

comp1.config()
comp2.config()
