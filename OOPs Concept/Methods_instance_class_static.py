# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 20:06:07 2020

@author: Mynuddin
"""
#Best article about this and serch on geeksforgeeks
#https://www.studytonight.com/post/methods-in-python-instance-class-and-static-method

class Student:
    
    school_name="Zoom University"
    
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
        
    #instance method    
    def avg(self):
        return (self.m1+self.m2+self.m3)/3
    
    @classmethod
    def info(cls):
        return cls.school_name

std1=Student(60,70,72)
std2=Student(70,75,89)

print(std1.avg())
print(std2.avg())
print(Student.info())









# Python program to demonstrate 
# instance methods  geeksforgeeks https://www.geeksforgeeks.org/instance-method-in-python/
    
class shape: 
      
    # Calling Constructor 
    def __init__(self, edge, color): 
        self.edge = edge 
        self.color = color 
          
    # Instance Method 
    def finEdges(self): 
        return self.edge 
          
    # Instance Method 
    def modifyEdges(self, newedge): 
        self.edge = newedge 
          
# Drive Code 
circle = shape(0, 'red') 
square = shape(4, 'blue') 
  
# Calling Instance Method 
print("No. of edges for circle: "+ str(circle.finEdges())) 
  
# Calling Instance Method 
square.modifyEdges(6) 
  
print("No. of edges for square: "+ str(square.finEdges())) 












#class method
#The classmethod() is an inbuilt function in Python, which returns a class method for a given function.
#Syntax: classmethod(function)
#def classMethod(cls, args...)
#https://www.programiz.com/python-programming/methods/built-in/classmethod#:~:text=A%20class%20method%20is%20a,and%20a%20class%20method%20is%3A&text=Class%20method%20works%20with%20the,is%20always%20the%20class%20itself.
class Person:
    age = 25

    def printAge(cls):
        print('The age is:', cls.age)

# create printAge class method 
Person.printAge = classmethod(Person.printAge)

Person.printAge()


"""
class Kerson:
    age = 25

    @classMethod
    def printAge(cls):
        print('The age is:', cls.age)

# create printAge class method 

Kerson.printAge()
"""




class Student: 
      
    # create a variable 
    name = "Geeksforgeeks"
      
    # create a function 
    def print_name(obj): 
        print("The name is : ", obj.name) 
          
# create print_name classmethod 
# before creating this line print_name() 
# It can be called only with object not with class 
Student.print_name = classmethod(Student.print_name) 
  
# now this method can be called as classmethod 
# print_name() method is called a class method 
Student.print_name()











#The @classmethod Decorator:
"""Syntax:

class C(object):
    @classmethod
    def fun(cls, arg1, arg2, ...):
       ....

fun: the function that needs to be converted into a class method
returns: a class method for function"""

# use of a class method and static method. 
from datetime import date 
  
class Person: 
    
    habit="Sucking code"
    
    def __init__(self, name, age): 
        self.name = name 
        self.age = age 
      
    # a class method to create a  
    # Person object by birth year. 
    @classmethod
    def fromBirthYear(cls, name, year): 
        return cls(name, date.today().year - year) 
    
    @classmethod  
    def chnage_habit(cls,h):
        cls.habit=h
        
      
    # a static method to check if a 
    # Person is adult or not. 
    @staticmethod
    def isAdult(age): 
        return age > 18
  
person1 = Person('mayank', 21) 
person2 = Person.fromBirthYear('mayank', 1996) 
  
print (person1.age) 
print (person2.age) 
  
# print the result 
print (Person.isAdult(22)) 
print(Person.habit)
Person.chnage_habit("fucking python")
print(Person.habit)

https://www.youtube.com/watch?v=PNpt7cFjGsM





"""Static methods in Python are extremely similar to python class level methods, 
the difference being that a static method is bound to a class rather than the objects
for that class.
This means that a static method can be called without an object for that class. 
This also means that static methods cannot modify the state of an object as they are
not bound to it."""

#its independent 
class Student:
    name = 'Student'
    def __init__(self, a, b):
        self.a = a
        self.b = b 
    
    @staticmethod
    def info():
        return "This is a student class"

print(Student.info())




class Calculator:

    # create addNumbers static method
    @staticmethod
    def addNumbers(x, y):
        return x + y

print('Product:', Calculator.addNumbers(15, 110))




class Calculator:

    def addNumbers(x, y):
        return x + y

# create addNumbers static method
Calculator.addNumbers = staticmethod(Calculator.addNumbers)

print('Product:', Calculator.addNumbers(15, 110))




















