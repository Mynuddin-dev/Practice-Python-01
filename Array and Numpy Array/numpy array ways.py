# -*- coding: utf-8 -*-
"""
Created on Thu May 14 09:50:05 2020

@author: Mynuddin
"""
# ways of define array
# array()    linespace()
#logspace()  arange()
#Zeroes()    ones()

import numpy as np
b1=np.array([6,7,8,3,4,5])    
b2=np.array([10,20,30,40,50],int)
print(b1)
print(b2)


#c1=np.linspace(1,10,10) start stop part dif same
#c1=np.linspace(1,15,10)
c1=np.linspace(1,15)
print(c1[5])
print(c1)
print(c1.dtype)


#its like a range   start stop step
d1=np.arange(1,20,2)
d2=np.arange(1,20)
d1
d2

npdata = np.arange(40) 
npdata.shape = (5, 8) #5 row 8 colmn
print(npdata)

print(np.arange(-8, -2, 2))
arr = np.arange(8) 
print("Original Array : \n", arr) 
  
# shape arr with 2 rows and 4 columns 
arr = np.arange(8).reshape(2, 4) 
print("\nArray reshaped with 2 rows and 4 columns : \n", arr) 
  
# shape arr with 2 rows and 4 columns 
arr = np.arange(8).reshape(4 ,2) 
print("\nArray reshaped with 4 rows and 2 columns : \n", arr) 
  
# Constructs 3D arr 
arr = np.arange(8).reshape(2, 2, 2) 
print("\nOriginal Array reshaped to 3D : \n", arr)

#logspace() way
#e=np.logspace(1,50,5)
#e=np.logspace(1,40,8)
e=np.logspace(1,50,10)  #1st and last as rule under part 
print(e)
print('%.2f'%e[0])



f=np.zeros(5)
f1=np.zeros(9,int).reshape(3,3)
f1

print(type(f1))
g=np.ones(5)
g

# zeroes and ones same 1 and 0 



# Creating an array from tuple
arr = np.array((1, 3, 2))
print("\nArray created using "
      "passed tuple:\n", arr)


# Create an array with random values 
e = np.random.random((2, 2)) 
print ("\nA random array:\n", e)

a = np.array([[1, 2, 4], [5, 8, 7]], dtype = 'float') 
print ("Array created using passed list:\n", a) 
  
# Creating array from tuple 
b = np.array((1 , 3, 2)) 
print ("\nArray created using passed tuple:\n", b) 
  
# Creating a 3X4 array with all zeros 
c = np.zeros((3, 4)) 
print ("\nAn array initialized with all zeros:\n", c) 


d = np.full((3, 3), 6, dtype = 'complex') 
print ("\nAn array initialized with all 6s." 
            "Array type is complex:\n", d) 

