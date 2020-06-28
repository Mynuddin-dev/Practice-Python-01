# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 05:49:03 2020

@author: Mynuddin
"""
#https://www.edureka.co/blog/inheritance-in-python/

#Single Inheritance
#When a child class inherits only a single parent class.

class Parent:
     def func1(self):
          print("this is function one")
class Child(Parent):
     def func2(self):
          print("this is function 2 ")
ob = Child()
ob.func1()
ob.func2()





#Multilevel Inheritance
#When a child class becomes a parent class for another child class.

class Parent:
      def func1(self):
          print("this is function 1")
class Child(Parent):
      def func2(self):
          print("this is function 2")
class Child2(Child):
      def func3(self):
          print("this is function 3")
          
ob = Child2()
ob.func1()
ob.func2()
ob.func3()





#Multiple Inheritance
#When a child class inherits from more than one parent class.

class Parent:
   def func1(self):
        print("this is function 1")
class Parent2:
   def func2(self):
        print("this is function 2")
class Child(Parent , Parent2):
    def func3(self):
        print("this is function 3")
 
ob = Child()
ob.func1()
ob.func2()
ob.func3()





#Hierarchical Inheritance
#Hierarchical inheritance involves multiple inheritance from the same base or parent class.

class Parent:
      def func1(self):
          print("this is function 1")
class Child(Parent):
      def func2(self):
          print("this is function 2")
class Child2(Parent):
      def func3(self):
          print("this is function 3")
 
ob = Child()
ob1 = Child2()
ob.func1()
ob.func2()

ob1.func1()
ob1.func3()






# Python program to demonstrate 
# hybrid inheritance 
  
  
class School: 
     def func1(self): 
         print("This function is in school.") 
   
class Student1(School): 
     def func2(self): 
         print("This function is in student 1. ") 
   
class Student2(School): 
     def func3(self): 
         print("This function is in student 2.") 
   
class Student3(Student1, School): 
     def func4(self): 
         print("This function is in student 3.") 
   
# Driver's code 
object = Student3() 
object.func1() 
object.func2() 







#Python Super() Function
#Super function allows us to call a method from the parent class.

class Parent:
     def func1(self):
         print("this is function 1")
class Child(Parent):
     def func2(self):
          Super().func1()
          print("this is function 2")
 
ob = Child()
ob.func2()





















