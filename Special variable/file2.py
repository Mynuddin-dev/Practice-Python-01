# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 19:46:57 2020

@author: Mynuddin
"""
import file1 
  
print("File2 __name__ = %s" %__name__ )
  
if __name__ == "__main__": 
    print("File2 is being run directly")
else: 
    print("File2 is being imported")