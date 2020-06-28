# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 20:43:27 2020

@author: Mynuddin

"""

class A:
    
    def __init__(self):
        print("__init__ function in 'A'")
        
    def feature1(self):
        print("Feature 1 is working")
        
    def feature2(self):
        print("Feature 2 is working")
  
class B(A):
    
    def feature3(self):
        print("Feature 3 is working")
        
    def feature4(self):
        print("Feature 4 is working")

a1=A()   #object of A class call the constructor of A class

b1=B()   #object of B class call the constructor of A class







class A:
    
    def __init__(self):
        print("__init__ function in 'A'")
        
    def feature1(self):
        print("Feature 1 is working")
        
    def feature2(self):
        print("Feature 2 is working")
  
class B(A):
    def __init__(self):
        print("__init__ function in 'B'")
    
    def feature3(self):
        print("Feature 3 is working")
        
    def feature4(self):
        print("Feature 4 is working")


b1=B()   # First call the B class constructor






#https://www.geeksforgeeks.org/python-super/
#The super function returns a temporary object of the superclass that allows access to all of its methods to its child class.
#Super()

class A:
    
    def __init__(self):
        print("__init__ function in 'A'")
        
    def feature1(self):
        print("Feature 1 is working")
        
    def feature2(self):
        print("Feature 2 is working")
  
class B(A):
    def __init__(self):
        
        super().__init__()    #super class feature
        print("__init__ function in 'B'")
    
    def feature3(self):
        print("Feature 3 is working")
        
    def feature4(self):
        print("Feature 4 is working")


b1=B()   # First call the B class constructor









#supper() in multiple inheritance
class A:
    
    def __init__(self):
        print("__init__ function in 'A'")
        
    def feature1(self):
        print("Feature 1 is working")
        
    def feature2(self):
        print("Feature 2 is working")
  
class B():
    def __init__(self):
        
        super().__init__()    #super class feature
        print("__init__ function in 'B'")
    
    def feature3(self):
        print("Feature 3 is working")
        
    def feature4(self):
        print("Feature 4 is working")


class C(A,B):
    def __init__(self):
        
        super().__init__()        #Method resulation order Left to Right
        
        print("__init__ function in 'C'") 
        
        
    def feature5(self):
        print("Feature 3 is working")
        
    def feature6(self):
        print("Feature 4 is working")
    

c1=C()






#for multiple inheritance
#in above example of method resulation oreder
## same thing also be for method

class A:
    
    def __init__(self):
        print("__init__ function in 'A'")
        
    def feature1(self):      #same method of class B
        print("Feature 1-A is working")
        
    def feature2(self):
        print("Feature 2 is working")
  
class B():
    def __init__(self):
        
        super().__init__()    #super class feature
        print("__init__ function in 'B'")
    
    def feature1(self):    # same function of class A
        print("Feature 1-B is working")
        
    def feature4(self):
        print("Feature 4 is working")


class C(A,B):
    def __init__(self):
        
        super().__init__()        #Method resulation order Left to Right
        
        print("__init__ function in 'C'") 
        
        
    def feature5(self):
        print("Feature 3 is working")
        
    def feature6(self):
        print("Feature 4 is working")
    

c1=C()
c1.feature1()












