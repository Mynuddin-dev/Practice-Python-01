# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 10:23:05 2020

@author: Mynuddin
"""
#https://www.geeksforgeeks.org/python-modules/ is also beauty
#Need to be set working directory

import calculate 
a=5
b=6

c = calculate.add(a,b)
print(c)



from calculate import*
A=5
B=6

c = mul(A,B)
print(c)




from calculate import div
i=30
j=6

c = div(i,j)
print(c)