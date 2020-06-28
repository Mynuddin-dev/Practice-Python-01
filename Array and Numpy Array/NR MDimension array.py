# -*- coding: utf-8 -*-
"""
Created on Thu May 14 09:50:05 2020

@author: Mynuddin
"""
import numpy as np
#----------------------Dimension of array-----------------

a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
a
print(a.ndim)
b
print(b.ndim)
c
print(c.ndim)
d
print(d.ndim)

a1=np.array([[1,2,3],
            [4,5,6]])

print(a1)
print(a1.dtype)
print(type(a1))
print(a1.sum())
print(a1.ndim)
print(a1.shape)
print(a1.size)

a2=a1.flatten()  #2D to 1D
print(a2)

print(a2.reshape(-1))

a2=a1.ravel()
print(a2)

# ---Differences between Flatten() and Ravel() | Numpy
# ravel() just like "shallow copy(view)" and flatten just like "deep copy"
'''a.ravel():
(i) Return only reference/view of original array
(ii) If you modify the array you would notice that the value of original array also changes.
(iii) Ravel is faster than flatten() as it does not occupy any memory.
(iv) Ravel is a library-level function.

a.flatten() :
(i) Return copy of original array
(ii) If you modify any value of this array value of original array is not affected.
(iii) Flatten() is comparatively slower than ravel() as it occupies memory.
(iv) Flatten is a method of an ndarray object.'''

a3=np.array(
    [[1,2,3,4,5,6],
     [7,8,9,3,2,4]])
print(a3.flatten())





a4=a3.reshape(3,2,2)   #3D array  2 x 2 3ta array
#1.kotoda array
#2.prottekta array te 1D array koyda = Row
#3 kotota value  = Col
print(a4)
a5=a3.reshape(2,3,2)   # 3 x 2   1 ta array 
print(a5)

print(len(a5))

print(a5.std())




























