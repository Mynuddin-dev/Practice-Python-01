# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 00:07:58 2020

@author: Mynuddin
"""
#https://www.datacamp.com/community/tutorials/inner-classes-python

class Student:
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll
        self.lap=self.Laptop()  #laptop class object

    def show(self):
        print(self.name,self.roll)
        lap1.show()

    class Laptop:
        def __init__(self):
            self.brand="HP"
            self.cpu="i5"
            self.ram="8gb"
        def show(self):
            print(self.brand,self.cpu,self.ram)
            
            
s1=Student("Jenny",1)
s2=Student("Melborn",7)
s1.show()
s2.show() 

#lap1=s1.lap
#print(lap1.brand)

#Directly creat an object in outside
lap1=Student.Laptop()
lap1.show()


