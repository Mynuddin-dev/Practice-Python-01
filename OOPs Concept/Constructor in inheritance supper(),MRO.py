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
#in above example of method resulation oreder (Constructor)
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











"""-----------------------------MRO-----------------------------------
#When we search for an attribute in a class that is involved in python 
#multiple inheritance, an order is followed. First, it is searched in the
#current class. If not found, the search moves to parent classes. This is
#left-to-right, depth-first

#So, in the above class, the search order will be – Child, Mother, Father, Object.

https://www.geeksforgeeks.org/method-resolution-order-in-python-inheritance/
www.srikanthtechnologies.com/blog/python/mro.aspx#:~:text=Method%20Resolution%20Order%20(MRO)%20is,lets%20examine%20a%20few%20cases.
https://stackoverflow.com/questions/1848474/method-resolution-order-mro-in-new-style-classes
https://www.geeksforgeeks.org/python-super/

"""


class G():
    def m(self):
        print("G")

class F(G):
    def m(self):
        print("F")
        super().m()

class E(G):
    def m(self):
        print("E")
        super().m()

class D(G):
    def m(self):
        print("D")
        super().m()

class C(E):
    def m(self):
        print("C")
        super().m()

class B(D, E, F):
    def m(self):
        print("B")
        super().m()

class A(B, C):
    def m(self):
        print("A")
        super().m()


#      A^
#     / \
#    B^  C^
#   /| X
# D^ E^ F^
#  \ | /
#    G







class I(G):
    def m(self):
        print("I")
        super().m()

class H():
    def m(self):
        print("H")

class G(H):
    def m(self):
        print("G")
        super().m()

class F(H):
    def m(self):
        print("F")
        super().m()

class E(H):
    def m(self):
        print("E")
        super().m()

class D(F):
    def m(self):
        print("D")
        super().m()

class C(E, F, G):
    def m(self):
        print("C")
        super().m()

class B():
    def m(self):
        print("B")
        super().m()

class A(B, C, D):
    def m(self):
        print("A")
        super().m()

# Algorithm:

# 1. Build an inheritance graph such that the children point at the parents (you'll have to imagine the arrows are there) and
#    keeping the correct left to right order. (I've marked methods that call super with ^)

#          A^
#       /  |  \
#     /    |    \
#   B^     C^    D^  I^
#        / | \  /   /
#       /  |  X    /   
#      /   |/  \  /     
#    E^    F^   G^
#     \    |    /
#       \  |  / 
#          H
# (In this example, A is a child of B, so imagine an edge going FROM A TO B)

# 2. Remove all classes that aren't eventually inherited by A

#          A^
#       /  |  \
#     /    |    \
#   B^     C^    D^
#        / | \  /  
#       /  |  X    
#      /   |/  \ 
#    E^    F^   G^
#     \    |    /
#       \  |  / 
#          H

# 3. For each level of the graph from bottom to top
#       For each node in the level from right to left
#           Remove all of the edges coming into the node except for the right-most one
#           Remove all of the edges going out of the node except for the left-most one

# Level {H}
#
#          A^
#       /  |  \
#     /    |    \
#   B^     C^    D^
#        / | \  /  
#       /  |  X    
#      /   |/  \ 
#    E^    F^   G^
#               |
#               |
#               H

# Level {G F E}
#
#         A^
#       / |  \
#     /   |    \
#   B^    C^   D^
#         | \ /  
#         |  X    
#         | | \
#         E^F^ G^
#              |
#              |
#              H

# Level {D C B}
#
#      A^
#     /| \
#    / |  \
#   B^ C^ D^
#      |  |  
#      |  |    
#      |  |  
#      E^ F^ G^
#            |
#            |
#            H

# Level {A}
#
#   A^
#   |
#   |
#   B^  C^  D^
#       |   |
#       |   |
#       |   |
#       E^  F^  G^
#               |
#               |
#               H

# The resolution order can now be determined by reading from top to bottom, left to right.  A B C E D F G H

x = A()
x.m(







