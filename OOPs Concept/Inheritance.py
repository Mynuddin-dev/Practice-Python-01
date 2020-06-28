# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 20:49:39 2020

@author: Mynuddin
"""

class A:
    def feature1(self):
        print("Feature 1 is working")
    def feature2(self):
        print("Feature 2 is working")
  
class B:
    def feature3(self):
        print("Feature 3 is working")
    def feature4(self):
        print("Feature 4 is working")

a1=A()
a1.feature1()
a1.feature2()




#Inheritance  and its single level

class A:                     #Thats the Super class or Parent class
    def feature1(self):
        print("Feature 1 is working")
    def feature2(self):
        print("Feature 2 is working")
  
class B(A): #inherited        Thats the Child class or derived class or sub class 
    def feature3(self):
        print("Feature 3 is working")
    def feature4(self):
        print("Feature 4 is working")

b1=B()
b1.feature1()
b1.feature2()
b1.feature3()
b1.feature4()



# its Multi level class

class A:                    
    def feature1(self):
        print("Feature 1 is working")
    def feature2(self):
        print("Feature 2 is working")
  
class B(A): #inherited
    def feature3(self):
        print("Feature 3 is working")
    def feature4(self):
        print("Feature 4 is working")

class C(B): #inherited
    def feature5(self):
        print("Feature 5 is working")
    def feature6(self):
        print("Feature 6 is working")


c1=C()
c1.feature1()
c1.feature2()
c1.feature3()
c1.feature4()
c1.feature5()
c1.feature6()









#Multiple Inheritance
class A:                    
    def feature1(self):
        print("Feature 1 is working")
    def feature2(self):
        print("Feature 2 is working")
  
class B: 
    def feature3(self):
        print("Feature 3 is working")
    def feature4(self):
        print("Feature 4 is working")

class C(A,B): #inherited A and B
    def feature5(self):
        print("Feature 5 is working")
    def feature6(self):
        print("Feature 6 is working")


c1=C()
c1.feature1()
c1.feature2()
c1.feature3()
c1.feature4()
c1.feature5()
c1.feature6()

























