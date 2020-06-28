# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 21:28:30 2020

@author: Mynuddin

Destructors are called when an object gets destroyed. In Python, destructors 
are not needed as much needed in C++ because Python has a garbage collector 
that handles memory management automatically

"""
#https://www.geeksforgeeks.org/destructors-in-python/?ref=lbp

class Employee: 
  
    # Initializing 
    def __init__(self): 
        print('Employee created.') 
  
    # Deleting (Calling destructor) 
    def __del__(self): 
        print('Destructor called, Employee deleted.') 
  
obj = Employee() 
del obj 









class Employee: 
  
    # Initializing  
    def __init__(self): 
        print('Employee created') 
  
    # Calling destructor 
    def __del__(self): 
        print("Destructor called") 
  
def Create_obj(): 
    print('Making Object...') 
    obj = Employee() 
    print('function end...') 
    return obj 
  
print('Calling Create_obj() function...') 
obj = Create_obj() 
print('Program End...') 