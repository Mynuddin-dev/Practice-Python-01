# -*- coding: utf-8 -*-
"""
Created on Sun May 31 09:33:27 2020

@author: Mynuddin

1.Required arguments or Positional arguments
2.Keyword arguments 
3.Default arguments
4.Variable-length arguments(*args)
5.kwargs

"""

""" ---------------- 1.Required or positional arguments----------------

Required arguments are the arguments passed to a function in correct positional
order. Here, the number of arguments in the function call should match exactly 
with the function definition.

we have to maintain sequential order thats are positional 

"""
def infome(name,age):
    print("Name ",name)
    print("Age ",age-1)

infome("Md Mynuddin",22)
# infome(22,"Md Mynuddin") error this line for position


""" What can i do if i dont know the function sequence of order or / and some 
where the function is created , in that case we use "keword arguments"
                                                    ==================
"""

def infome(name,age):
    print("Name ",name)
    print("Age ",age-1)

infome(age=22,name="Md Mynuddin") 




"""--------------------------Default arguments----------------------------
A default argument is an argument that assumes a default value if a value is
 not provided in the function call for that argument."""

def printinfo( name, age = 35 ):
   print ("Name: ", name)
   print ("Age ", age)
   return

# Now you can call printinfo function
printinfo( age=50, name="miki" )
printinfo( name="miki" ) # need to be pass 2 parameter but one provided 
                         # that case work default arguments



"""---------------------Variable length argument---------------------------
 You are define a function where the number of argument is not fixed """
#It is used to pass a non-keyworded, variable-length argument list.

# Function definition is here
def printinfo( arg1, *vartuple ):
   print( "Output is: ")
   print ("arg1 :",arg1)
   for var in vartuple:
      print (var,end=" ")
   return;

# Now you can call printinfo function
printinfo( 10 )
printinfo( 70, 60, 50,80, 90, 20)

def add(a,*b):        #receive argument as a tuple  (*b)
    print("a :",a)
    print("b :",b) 
    print(type(b))
    print("Sum :",a+sum(b))

add(1,2,3,4,5,6,7,8,9,10)




def myFun(*argv):  
    for arg in argv:  
        print (arg)    
myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks') 


def myFun(arg1, *argv): 
    print ("First argument :", arg1) 
    for arg in argv: 
        print("Next argument through *argv :", arg) 
  
myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks') 



"""--------------------------**kwargs-------------------------"""
# This way the function will receive a ""dictionary of arguments"", 
# and can access the items accordingly:
# *kargs for variable number of  ""keyword arguments""  
def myFun(**kwargs):
    a=kwargs.keys()
    b=kwargs.values()
    print(a)
    print(b)
    print(kwargs)
    print(type(kwargs))
    for key, value in kwargs.items():  
        print ("%s == %s" %(key, value)) 
        
# Driver code 
myFun(first ='Geeks', mid ='for', last='Geeks') 


def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")



def info(x,**y):
    print(x)
    for i,j in y.items():
        print(i,j)
    
info("Md Mynuddin Learning python from",age=22,date="Monday 10 ,2020")


def myFun(*args,**kwargs): 
    print("args: ", args) 
    print("kwargs: ", kwargs) 
    print("args :",type(args))
    print("kwargs :",type(kwargs))
  
# Now we can use both *args ,**kwargs to pass arguments to this function : 
myFun(3,4,5,6,7,2, first="Geeks",mid="for",last="Geeks") 

 







