# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 09:10:48 2020

@author: Mynuddin
"""

class Computer:
    def __init__(self):
        self.name="Mynuddin"
        self.age=21
    #def update(self):       #self received c1 as a object
         #self.age=28

    def compare(self,others):
        if self.age==others.age:
            return True
        else:
            return False
        
        
c1=Computer()
c1.age=23
c2=Computer() 

if c1.compare(c2):
    print("They are same")
else:
    print("They aren't same")


"""c1.name="Alex"
c1.age=12
c1.update()#go to the update function arg =c 1

print(c1.name)
print(c2.name)

# whats the size of the object ?depends no of variable and size of each 
# who is resposible to calculate the memory or who allowcates size to object 
# that is Constructor 
print(id(c1))
print(id(c2)) """