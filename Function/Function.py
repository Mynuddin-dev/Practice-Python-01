# -*- coding: utf-8 -*-
"""
Created on Sat May 30 18:22:20 2020

@author: Mynuddin
"""
def great():
    print("Good Morning")
    print("Md Mynuddin")
    
great()  

def add(x,y):
    a=x+y
    b=x-y
    return a,b

result1,result2 = add(8,4)
print(result1,result2)

#--------Passed by Referance vs Passed by value-----------

def modify(x):
    x=8
    print(x)
    
modify(10)

''' ---------------Actually Avobe all-----------------------------
 All parameters (arguments) in the Python language are passed by
 reference.It means if you change what a parameter refers to within 
 a function, the change also reflects back in the calling function.'''


 
'''                     Pass-by-value
In pass-by-value, the function receives a copy of the argument objects 
passed to it by the caller, stored in a new location in memory.
Doesn't Effect each other .Passed only alue not address.

the passing is like call-by-value because you can not change the valueof the immutable 
objects being passed to the function.'''

def modify(x):   
    print(id(x))
    x=8
    print(id(x))
    print("x ",x)
 
a=10
print(id(a))
modify(a)
print("a ", a)


def changeme( mylist ):
   print("This changes a passed list into this function")
   print(id(mylist))
   print(mylist)
   mylist = [1,2,3,4] # This would assig new reference in mylist
   print(id(mylist))
   print ("Values inside the function: ", mylist)
   
# Now you can call changeme function
mylist = [10,20,30]
print(id(mylist))
changeme( mylist )
print ("Values outside the function: ", mylist)


# call by value   
string = "Geeks" 
def test(string): 
      
    string = "GeeksforGeeks"
    print("Inside Function:", string) 
# Driver's code 
test(string) 
print("Outside Function:", string)

 
# --------------------------call by reference---------------------------- 
'''Whereas passing mutable objects can be considered as call by reference 
because when their values are changed inside the function, then it will also
be reflected outside the function. 

In pass-by-reference, the box (the variable) is passed directly into the 
function, and its contents (the object represented by the variable) 
implicitly come with it. Inside the function context, the argument is 
essentially a "complete alias" for the variable passed in by the caller.
They are both the exact same box, and therefore also refer to the exact
                        "same object in memory".
'''


def add_more(list): 
    print(id(list))
    list.append(50) 
    print(id(list))
    print("Inside Function", list) 
  
# Driver's code  list is mutable
mylist = [10,20,30,40] 
print(id(mylist)) 
add_more(mylist) 
print("Outside Function:", mylist) 



'''Binding Names to Objects In python, each variable to which we assign a 
value/container is treated as an object. When we are assigning a value to 
a variable, we are actually binding a name to an object.'''

a = "first"
b = "first"  
# Returns the actual location  
# where the variable is stored 
print(id(a))   
# Returns the actual location  
# where the variable is stored 
print(id(b)) 
# Returns true if both the variables 
# are stored in same location 
print(a is b)


a = [10, 20, 30] 
b = [10, 20, 30]  
# return the location 
# where the variable  
# is stored 
print(id(a))   
# return the location 
# where the variable  
# is stored 
print(id(b)) 
# returns false if the 
# location is not same 
print(a is b) 


"""The output of the above two examples are different because the list is 
mutable and the string is immutable. An immutable variable cannot be changed
once created. If we wish to change an immutable variable, such as a string,
we must create a new instance and bind the variable to the new instance. 
Whereas, mutable variable can be changed in place"""