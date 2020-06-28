# -*- coding: utf-8 -*-
"""
Created on Thu May 28 00:34:08 2020

@author: Mynuddin
"""
import numpy as np

arr1 = np.array([1, 2, 3])

for x in arr1:
  print(x)

arr2 = np.array([[1, 2, 3], [4, 5, 6]])

for x in arr2:
  print(x)
  
#--------Iterate on each scalar element of the 2-D array -----
for x in arr2:
    for y in x:
        print(y)
        
arr3 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])


for x in arr3:
    print(x)
    
for x in arr3:
  for y in x:
    for z in y:
      print(z)
#------------------------------------------------------------      
      
for x in np.nditer(arr3) :
    print(x)     
      
arr = np.array([1, 2, 3])

for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
  print(x)     
      
arr4 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

for x in np.nditer(arr4[:, ::2]):
  print(x)     
    
  
for idx, x in np.ndenumerate(arr4):   # index based
    print(idx, x)    
print(arr4.shape)     
      