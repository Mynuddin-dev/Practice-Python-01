# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 08:30:28 2020

@author: Mynuddin

-------Python lambda (Anonymous Functions) | filter, map, reduce----------

In Python, anonymous function means that a function is without a name.
As we already know that def keyword is used to define the normal functions
and the lambda keyword is used to create anonymous functions. It has the
following syntax:

-----------------lambda arguments: expression-------geeksforgeeks follow--

"""

sum = lambda arg1, arg2: arg1 + arg2;

# Now you can call sum as a function
print ("Value of total : ", sum( 10, 20 ))
print ("Value of total : ", sum( 20, 20 ))


# showing difference between def() and lambda(). 
def cube(y): 
    return y*y*y; 
  
g = lambda x: x*x*x 
print(g(7)) 
print(cube(5)) 





# How to use map filter and reduce
# http://net-informations.com/python/iq/map.htm and navin raddy

"""---------------------------Filter-----------------------"""
def even(x):
   return x%2==0      

li=[1,2,3,4,5,6,7,8,9,10]    

evens=list(filter(even,li))
print(evens)

    



li=[1,2,3,4,5,6,7,8,9,10]    

evens=list(filter(lambda x : x%2==0 ,li))
print(evens)

doubles=list(map(lambda n : n*2,evens))
print(doubles)

from functools import reduce
operation=reduce(lambda a,b : a+b,doubles)
print(operation)





