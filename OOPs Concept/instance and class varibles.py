# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 11:06:41 2020

@author: Mynuddin
"""
class Employee:
    increment=1.5      #class variable 
    no_of_employee=0
    def __init__(self,fname,lname,salary):
        self.fname=fname
        self.lname=lname
        self.salary=salary
        self.increment=1.4    #instance variable
        Employee.no_of_employee +=1
        
    def increase(self):
        #self.salary = self.salary*Employee.increment use class variable
        #self.salary = self.salary*self.increment      #first search in instance
                                                      #variable if not find take
                                                      #class variable

        self.salary = self.salary*self.increment
print(Employee.no_of_employee)
harray=Employee("Harry","Potter",44000)
print(Employee.no_of_employee)
rohan=Employee("Rohan","Sharma",55000)   
print(Employee.no_of_employee)

 
print(harray.salary)
harray.increase()
print(harray.salary)      

   
#print(harray.fname,rohan.fname)  
print(Employee.__dict__)  
print(harray.__dict__)  #instance variable print  
