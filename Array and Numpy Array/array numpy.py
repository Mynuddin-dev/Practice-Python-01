''' I think the yellow warning  is not a problem 
    its recomended the specefic module to use 
    if import* that is not to specify or your machine may be not 
    to install the full packages
'''
#also normally created array() use
#dont need to specify type auto convert
import numpy as np   
ar=np.array([1,2,3,4,5])

ar1=ar+5
print(ar1) 

ar2=ar1+ar
print(ar2)

ar3=ar1-ar
print(ar3)

print(np.sin(ar))
print(np.cos(ar)) 
print(np.log(ar))
print(np.sqrt(ar))


print(np.sum(ar)," ",min(ar)," ",max(ar))
print(np.concatenate([ar,ar1]))

# Some normal math operation

a = np.array([[1, 2],
              [3, 4]])
print(a.T)
# Defining Array 2
b = np.array([[4, 3],
              [2, 1]])
print(b.T)

#--print(numpy.transpose(matrix))
               
# ------------Adding 1 to every element------------

print ("Adding 1 to every element:", a + 1)
 
print ("\nSubtracting 2 from each element:", b - 2)

print ("\nSum of all array "
       "elements: ", a.sum())
 
print ("\nArray sum:\n", a + b)

# multiply each element by 10 
print ("Multiplying each element by 10:", a*10) 
  
# square each element 
print ("Squaring each element:", a**2) 
  
# modify existing array 
a *= 2
print ("Doubled each element of original array:", a) 
  

f=np.add(a,b)
print(f)

# multiply arrays (elementwise multiplication) 
print ("Array multiplication:\n", a*b) 
  
# matrix multiplication 
print ("Matrix multiplication:\n", a.dot(b)) 

print ("\nArray sum:\n", a / b)

# --------------Universal functions -------------------------

# create an array of sine values 
a = np.array([0, np.pi/2, np.pi]) 
print ("Sine values of array elements:", np.sin(a)) 

# exponential values 
a = np.array([0, 1, 2, 3]) 
print ("Exponent of array elements:", np.exp(a)) 
  
# square root of array values 
print ("Square root of array elements:", np.sqrt(a))

'''----------------Sorting array--------------------'''

a = np.array([[1, 4, 2], 
                 [3, 4, 6], 
              [0, -1, 5]]) 
  
# sorted array 
print ("Array elements in sorted order:\n", 
                    np.sort(a, axis = None)) 
  
# sort array row-wise 
print ("Row-wise sorted array:\n", 
                np.sort(a, axis = 1)) 
  
# specify sort algorithm 
print ("Column wise sort by applying merge-sort:\n", 
            np.sort(a, axis = 0, kind = 'mergesort')) 
  
# Example to show sorting of structured array 
# set alias names for dtypes 
dtypes = [('name', 'S10'), ('grad_year', int), ('cgpa', float)] 
  
# Values to be put in array 
values = [('Hrithik', 2009, 8.5), ('Ajay', 2008, 8.7),  
           ('Pankaj', 2008, 7.9), ('Aakash', 2009, 9.0)] 
             
# Creating array 
arr = np.array(values, dtype = dtypes) 
print ("\nArray sorted by names:\n", 
            np.sort(arr, order = 'name')) 
              
print ("Array sorted by grauation year and then cgpa:\n", 
                np.sort(arr, order = ['grad_year', 'cgpa']))




'''============ Constructing a Datatype Object ===============
In Numpy, datatypes of Arrays need not to be defined unless a
specific datatype is required. Numpy tries to guess the datatype
for Arrays which are not predefined in the constructor function.

# Python Program to create
# a data type object'''
 
# Integer datatype
# guessed by Numpy
x = np.array([1, 2])  
print("Integer Datatype: ")
print(x.dtype)         
 
# Float datatype
# guessed by Numpy
x = np.array([1.0, 2.0]) 
print("\nFloat Datatype: ")
print(x.dtype)  
 
# Forced Datatype
x = np.array([1, 2], dtype = np.int64)   
print("\nForcing a Datatype: ")
print(x.dtype)
#-----------------Copy an array----------------

a1=np.array([2,3,4,5,6])

'''a2=a1          #Aliasing same addr same value

a2=a1.view()   #diffrenet addr same valu
a1[2]=9        #Shallow copy both are dependent each other'''

a2=a1.copy()   #Deep  copy not dependent each other

print(a1)
print(a2)
print(id(a1))
print(id(a2))






