# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 10:02:37 2020

@author: Mynuddin
"""
class car:
    
    wheel=4                #class variable .if its change the whole file where
                           # it use its effect 
    
    def __init__(self):
        self.name="BMW"    # thats are instance variable
        self.speed=78      # if theirs varible change doesn't efeect other 


car1=car()
car1.speed=68
car2=car()

car.wheel=5                # Effect everywhere

print(car1.name,car2.speed,car.wheel)
print(car2.name,car2.speed,car.wheel)
