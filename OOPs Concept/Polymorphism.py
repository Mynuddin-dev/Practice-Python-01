# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 12:18:31 2020

"----------------------------Duck typing------------------------------------"
 
in computer programming is an application of the duck test— 

"If it walks like a duck and it quacks like a duck, then it must be a duck"— 

to determine if an object can be used for a particular purpose.

In duck typing, an object's suitability is determined by the presence of 
certain methods and properties, rather than the type of the object itself."""

#https://www.geeksforgeeks.org/duck-typing-in-python/#:~:text=Duck%20Typing%20is%20a%20type,a%20given%20method%20or%20attribute.



class PyCharm:
    def execute(self):
        print("Compiling and Runing in PyCharm")


class Spyder:
    def execute(self):
        print("Its also Running well in spyder")
        print("Check spell and correct")
        print("kite use in spyder also")


class Laptop:
    def coding(self,ide): #doesnt matter which classes obj passing
                          #the matter is the object should be execute method
        ide.execute()
        
        
#ide=PyCharm()     
ide=Spyder()


Lap1=Laptop()
Lap1.coding(ide)








#operator overloading
#Details in this link
#https://www.geeksforgeeks.org/operator-overloading-in-python/

a=5
b=6
print(a+b)
print(int.__add__(a,b))

a="5"
b="6"
print(a+b)
print(str.__add__(a,b))
# __mul__
# __sub__
# __divmod__


class Student:  
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
        
    def __add__(self,other):
    
        m1=self.m1 + other.m1
        m2=self.m2 + other.m2
        s3=Student(m1,m2)
        return s3
    
    def __gt__(self,others):
        k1=self.m1 +self.m2
        k2=others.m1 + others.m2
        if k1>k2:
            return True
        else:
            return False
        


s1=Student(45,45)
s2=Student(50,56) 

s3=s1+s2     #Student.__add__(s1,s2)
             #class dont know how to add
print(s3.m1)

if s1>s2:
    print("S1 is Greater than S2")
    
else:
    print("S2 is Greater than S1")

print(s1)  #address
print(s3)
 

#------------------------------Method Overloading-----------------------------
#Overloading: Overloading occurs when two or more methods in one class have
#the same method name but different parameters.

class Person:
    def Hello(self, name=None):
        if name is not None:
            print('Hello ' + name)
        else:
            print('Hello ')
# Create instance
obj = Person()
# Call the method
obj.Hello()
# Call the method with a parameter
obj.Hello('Edureka')








class Compute:
# area method in edureka website its explain details
    def area(self, x = None, y = None):
        if x != None and y != None:
            return x * y
        elif x != None:
            return x * x
        else:
            return 0
# object
obj = Compute()
# zero argument
# one argument 
print("Area Value:", obj.area(4))
# two argument
print("Area Value:", obj.area(3, 5))





#https://www.geeksforgeeks.org/python-method-overloading/
class calculate:
    
    def product(self,a, b): 
        p = a * b 
        print(p) 
          
# Second product method 
# Takes three argument and print their 
# https://stackoverflow.com/questions/10202938/how-do-i-use-method-overloading-in-python
    def product(self,a, b, c): 
        p = a * b*c 
        print(p) 
      
a1=calculate() 

#a1.product(4, 5) # Uncommenting the below line shows an error    
a1.product(4, 5, 5)# This line will call the second product method 








#for the above problem  ""But its not efficient""
# Function to take multiple arguments 
def add(datatype, *args): 
  
    # if datatype is int 
    # initialize answer as 0 
    if datatype =='int': 
        answer = 0
          
    # if datatype is str 
    # initialize answer as '' 
    if datatype =='str': 
        answer ='' 
  
    # Traverse through the arguments 
    for x in args: 
  
        # This will do addition if the  
        # arguments are int. Or concatenation  
        # if the arguments are str 
        answer = answer + x 
  
    print(answer) 
  
# Integer 
add('int', 5, 6) 
  
# String 
add('str', 'Hi ', 'Geeks') 









# Multiple Dispatch Decorator ""Efficient one

from multipledispatch import dispatch 
class calc:  
    #passing one parameter 
    @dispatch(int,int) 
    def product(first,second): 
        result = first*second 
        print(result); 
      
    #passing two parameters 
    @dispatch(int,int,int) 
    def product(first,second,third): 
        result  = first * second * third 
        print(result); 
      
    #you can also pass data type of any value as per requirement 
    @dispatch(float,float,float) 
    def product(first,second,third): 
        result  = first * second * third 
        print(result); 
      
AB=calc() 
#calling product method with 2 arguments 
AB.product(2,3,2) #this will give output of 12 
AB.product(2.2,3.4,2.3) # this will give output of 17.985999999999997










#-------------------------Method Overriding------------------------------------
#Overriding: Overriding means having two methods with the same method name and
#parameters (i.e., method signature). One of the methods is in the parent class
#and the other is in the child class.
#https://www.studytonight.com/python/method-overriding-in-python
#https://www.geeksforgeeks.org/method-overriding-in-python/

class Dad:
    def phone(self):
        print("In 2005  My father used Nokia-1110")

class me(Dad):
    def my_phone(self):
        print("This time i have no phone")
    def phone(self):
        print("i override my dad phone and my phone is now 'oppo reno z'")
        
a=me()
a.dad_phone()





 

# parent class
class Animal:
  # properties
	multicellular = True
	# Eukaryotic means Cells with Nucleus
	eukaryotic = True
	
	# function breath
	def breathe(self):
	    print("I breathe oxygen.")
    
  # function feed
	def feed(self):
	    print("I eat food.") 
	    
# child class	    
class Herbivorous(Animal):
    
    # function feed
	def feed(self):
	    print("I eat only plants. I am vegetarian.")

herbi = Herbivorous()
herbi.feed()   #overriding
# calling some other function
herbi.breathe()






#geeksforgeeks
#Defining parent class 
class Parent(): 
      
    # Constructor 
    def __init__(self): 
        self.value = "Inside Parent"
          
    # Parent's show method 
    def show(self): 
        print(self.value) 
          
# Defining child class 
class Child(Parent): 
      
    # Constructor 
    def __init__(self): 
        self.value = "Inside Child"
          
    # Child's show method 
    def show(self): 
        print(self.value) 
          
          
# Driver's code 
obj1 = Parent() 
obj2 = Child() 

obj2.show() #ovverride

obj1.show() 








#Method overriding with multiple and multilevel inheritance
#Defining parent class 1 
class Parent1(): 
          
    # Parent's show method 
    def show(self): 
        print("Inside Parent1") 
          
# Defining Parent class 2 
class Parent2(): 
          
    # Parent's show method 
    def display(self): 
        print("Inside Parent2") 
          
          
# Defining child class 
class Child(Parent1, Parent2): 
          
    # Child's show method 
    def show(self): 
        print("Inside Child") 
     
        
# Driver's code 
obj = Child() 
  
obj.show() 
obj.display()








# overriding in multilevel inheritance  
 
class Parent():  
        
    # Parent's show method 
    def display(self): 
        print("Inside Parent") 
    
     
# Inherited or Sub class (Note Parent in bracket)  
class Child(Parent):  
        
    # Child's show method 
    def show(self): 
        print("Inside Child") 
    
# Inherited or Sub class (Note Child in bracket)  
class GrandChild(Child):  
          
    # Child's show method 
    def show(self): 
        print("Inside GrandChild")          
    
# Driver code  
g = GrandChild()    
g.show() 
g.display() 






# calling the parent's class method 
# inside the overridden method  using class name

class Parent(): 
      
    def show(self): 
        print("Inside Parent") 
          
class Child(Parent): 
      
    def show(self): 
          
        # Calling the parent's class 
        # method 
        Parent.show(self) 
        print("Inside Child") 
          
# Driver's code 
obj = Child() 
obj.show() 





# calling the parent's class method 
# inside the overridden method using 
# super() 
   
class Parent(): 
      
    def show(self): 
        print("Inside Parent") 
          
class Child(Parent): 
      
    def show(self): 
          
        # Calling the parent's class 
        # method 
        super().show() 
        print("Inside Child") 
          
# Driver's code 
obj = Child() 
obj.show() 


