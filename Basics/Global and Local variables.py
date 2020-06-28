# -*- coding: utf-8 -*-
"""
Created on Sun May 31 21:13:28 2020

@author: Mynuddin

 Global variables are the one that are defined and declared outside a function
 and we need to use them inside a function.
 
 Variables that are defined inside a function body have a local scope This 
 means that local variables can be accessed only inside the function
 
"""

a=10        #as a global variable

def fun():
    # print(a) 
    
    a=20    #as a local variable
    print("Inside the function:",a)
    
fun()    
print("Outside the function:",a) 



a=10

def fun():

    print("Inside the function:",a) #use directly the global variable
    
fun()    
print("Outside the function:",a) 



""" if we change the value of global variable as a global inside of the function
--------------------------use "global" keyword ---------------------------"""
a=10

def fun():
    global a 
    print(a)
    a=15
    print("Inside the function:",a) 
    
fun()    
print("Outside the function:",a) 


#Used local and global variable in the same function
a=10
print(id(a))
b=90
c=80
def fun():
    
    a=15 
    x=globals()["a"]
    print("x=",x)
    print(id(x))
    print("Inside the function:",a) 
    #globals()["a"]=40
    
fun()    
print("Outside the function:",a) 


# This function modifies the global variable 's' 
# Global Scope  
s = "Python is great!" 
def f(): 
    global s
    print(s)
    s = "Look for Geeksforgeeks Python Section"
    print(s)  

f() 
print(s) 


"""------------------------A good example--------------------------"""

a = 1
# Uses global because there is no local 'a' 
def f(): 
    print ('Inside f() : ', a )
  
# Variable 'a' is redefined as a local 
def g():     
    a = 2
    print ('Inside g() : ',a )
  
# Uses global keyword to modify global 'a' 
def h():     
    global a 
    a = 3
    print ('Inside h() : ',a )
  
# Global scope 
print ('global : ',a )
f() 
print ('global : ',a )
g() 
print ('global : ',a )
h() 
print ('global : ',a )




