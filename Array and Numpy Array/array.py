from array import * #need specified
'''arrayName = array(typecode, [Initializers])'''
import array as arr  
# =============================================================================
#  
# =============================================================================
ab=arr.array('i',[1,2,3,4,5,-6,0])   #sign int - 0 +
abc=arr.array('I',[1,2,3,4,5,6])     #unsign int only + value
print(ab)
print(ab.buffer_info())
print(abc)
print(abc.typecode)


# creating an array with integer type 
a = arr.array('i', [1, 2, 3]) 
     
# printing original array  
print ("The new created array is : ", end =" ") 
for i in range (0, 3): 
    print (a[i], end =" ") 
print() 
  
# creating an array with float type  
b = arr.array('d', [2.5, 3.2, 3.3]) 
  
# printing original array 
print ("The new created array is : ", end =" ") 
for i in range (len(b)): 
    print (b[i], end =" ")
    

a.append(4)
print(a)
a.insert(1,9)
print(a)

print ("Array after insertion : ", end =" ") 
for i in (a): 
    print (i, end =" ") 
print()  
  
# array with float type 
b = arr.array('d', [2.5, 3.2, 3.3]) 
  
print ("Array before insertion : ", end =" ") 
for i in range (0, 3): 
    print (b[i], end =" ") 
print() 
  
# adding an element using append() 
b.append(4.4) 
  
print ("Array after insertion : ", end =" ") 
for i in (b): 
    print (i, end =" ") 
print()  

print(a[3])
print(b[-3])

a.reverse()
print(a)    
a.count(3)

a.pop(2)
print(a)

# using remove() to remove 1st occurrence of 1 
a.remove(1) 
print(a)
del(abc)

bk=arr.array(a.typecode,(a for a in ab))
k=arr.array(a.typecode,a)
print(bk)
print(k)

print(bk[2:7])
print(bk[3:])
print(bk[:5])
print(bk[:])
print(bk[:-1])
print(bk[::-1])
bk[5]=6  #update
print(bk)

#---------------array user input-----------------------------
t=arr.array('i',[])
n=int(input("Please enter the length of array : "))
print("Please enter the array values : ")
for i in range(n):
    x=int(input())
    t.append(x)
    
print(t)   
    
#---------------searching an element in an array-------------
m=int(input("Please enter your searching number :"))

#print("The index of",m," is :",t.index(m))

l=0
for i in t:
    if i==m:
        print("The index of",m," is :",l)
        break
    l=l+1
        
#----------------NumPy array searching (index) ------------
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 4, 4])

#x = np.where(arr == 4)
#x = np.where(arr%2 == 0)  
x = np.where(arr%2 == 1)
  
print(x) 


'''There is a method called searchsorted() which performs a binary search 
in the array, and returns the index where the specified value would be 
inserted to maintain the search order. The searchsorted() method is assumed
to be used on sorted arrays.'''

arr2 = np.array([6, 7, 8, 9])

x = np.searchsorted(arr2, 7)
#x = np.searchsorted(arr, 7, side='right')

print(x)

#Find the indexes where the values 2, 4, and 6 should be inserted:
arr3 = np.array([1, 3, 5, 7])
x = np.searchsorted(arr3, [2, 4, 6])

print(x)



