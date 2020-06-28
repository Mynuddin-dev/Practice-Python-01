# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 13:45:56 2020

@author: Mynuddin 
"""

message = "Hello Python Crash Course world!"
print(message)
print("Hello String\n")

'''------------------------user input------------------------'''

a= input("Please enter something 1st:")
print(type(a))
b= input("Please enter something 2nd:") 
print(type(b))
print(a+b)

a=int(input("Please Enter 1st Value: "))
b=int(input("Please Enter 2nd value: "))
print(a+b)

c=input("Enter a character:")#[0]
print(c)
print(c[0])


result=eval(input("Enter an Exprression : "))
print(result)

'''------------------------------If Else--------------------------'''

x=int(input("Please enter any number : "))
if x%2==0:
    print( x, "is even.")
else:
    print(x, "is odd.")
print("Good Bye Thank You \U0001f602")    

a=int(input("Please Enter 1st value : "))
b=int(input("Please Enter 2nd value : "))
c=int(input("Please Enter 3rd value : "))

if a>b:
    if a>c:
        print(a,"IS GREATER")
    else:
        print(c,"IS  GREATER")
elif a<b:
    if c<b:
        print(b,"IS GREATER")
    else:
        print(c, "IS GREATER")

'''-----------------------while loop----------------------------------'''
i=1
while i<=5:
    print("Md Mynuddin ", end="")
    j=1
    while j<=4:
        print(" Rocks", end="")
        j+=1
    i+=1
    print()

'''-----------------------for loop----------------------------------'''

l=["ME",3.68,4]

for i in l:
    print(i)

for i in ["MYNUDDIN",3.70,4]:
    print(i)

for i in "MNKGR":
    print(i)

for i in range(10):
    print(i ,end=" ")

for i in range(11,21,2):
    print(i)

for i in range(21,10,-2):
    print(i)
    
for i in range(21 , 11 , -2):
    print(i)
    
for i in range(10 , 21 , 1):
    if(i%5==0):
        print(i)
    
for i in range(1,11,1):
    print("5 * ",i,"=", 5*i)

'''----------------------Break  and continue--------------------'''
for i in range(1,11,1):
    if i%2==0:
        continue 
    print("5 * ",i,"=", 5*i)
    
    
for i in range(1,11,1):
    if i==5:
        break
    print("5 * ",i,"=", 5*i)   
    
    
x=int(input("How many candies you want? :"))
available=10
i=1
while i<=x:
    if x>available:
        print("Sorry Out Of Stock")
        break
    elif i<=available:
        print("Your Candy")
    i=i+1

print("Byeeeeeee")    

'''----------------------------pattern---------------------------------'''

for i in range(5):
    for j in range(5):
        print("* ",end="")
    print()  
    

for i in range(5):
    for j in range(5):
        if i>=j:
            print("* ",end="")
    print()    

for i in range(5):
    for j in range(5):
        if i<=j:
            print("* ",end="")
    print()
 
    
for i in range(1,5,1):
    for j in range(i):
            print("* ",end="")
    print()
    
