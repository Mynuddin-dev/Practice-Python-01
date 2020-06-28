# -*- coding: utf-8 -*-
"""
Created on Thu May 28 00:52:57 2020

@author: Mynuddin
 ----- there stack and concatenate i m not clear
"""

import numpy as np 

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])
print ('Joining the two arrays along axis 0:' )

arr = np.concatenate((arr1, arr2))

print(arr)

arr1 = np.array([[1, 2],
                 [3, 4]])

arr2 = np.array([[5, 6],
                 [7, 8]])
 
print ('Joining the two arrays along axis 1:' )
arr = np.concatenate((arr1, arr2), axis=1)
#arr = np.concatenate((arr1, arr2), axis=0) #0 axis

arr = np.stack((arr1, arr2), axis=1)

arr = np.vstack((arr1, arr2))
arr = np.hstack((arr1, arr2))
arr = np.dstack((arr1, arr2))

print(arr)

