# -*- coding: utf-8 -*-
"""
Created on Sun May 31 22:18:00 2020

@author: Mynuddin

"""


def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact 
    
x=int(input("Please enter your value:"))

result=factorial(x)
print("The factorial of", x," is :",result)



