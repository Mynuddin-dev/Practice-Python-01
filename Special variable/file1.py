# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 19:43:01 2020

@author: Mynuddin
"""          
#point of execution ,start the code


print ("File1 __name__ = %s" %__name__) 
  
if __name__ == "__main__": 
    print ("File1 is being run directly")
else: 
    print ("File1 is being imported")