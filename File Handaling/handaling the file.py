# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 08:31:16 2020

@author: Mynuddin
"""

f=open('First.txt','r') # read only
#f=open('F:\IIT,BSSE\Fourth Semister\Python\Pracctice\File Handaling\First.txt','r')
#print(f.read())
#print(f.read(5))
#print(f.readline())
#print(f.readline())
#print(f.readlines())
#f = open("foo.txt", "wb")
#print "Name of the file: ", f.name
#print "Closed or not : ", f.closed
#print "Opening mode : ", f.mode
#print "Softspace flag : ", f.softspace
# Close opend file
#f.close()


f1=open('second.txt','r+') #Working with "Reading and Writing" in the text
#print(f1.read())
f1.write(" you can read an existing file and write something also")
print(f1.read())

#previous text gone
f1.close()



f2=open('3rd.txt','rb+') 
print(f2.read())
f2.close()


# Python code to illustrate append() mode 
file = open('ABC.txt','r') 
print(file.read())
file2 = open('ABC.txt','a')  
print(file2.write("This will add this line"))
print(file.read()) 
file.close()




file1=open('Write.txt','w')  #if there is not Write.txt file than creat it auto
print(file1.write("Writing somethings"))
file1.close()

file2=open('WR','w+')
print(file2.write("Writing and Reading permission granted"))
print(file2.read())




"""The access modes available for the open() function are as follows:
    
https://stackabuse.com/file-handling-in-python/

r: Opens the file in read-only mode. Starts reading from the beginning of the file and is the default mode for the open() function.
rb: Opens the file as read-only in binary format and starts reading from the beginning of the file. While binary format can be used for different purposes, it is usually used when dealing with things like images, videos, etc.
r+: Opens a file for reading and writing, placing the pointer at the beginning of the file.
w: Opens in write-only mode. The pointer is placed at the beginning of the file and this will overwrite any existing file with the same name. It will create a new file if one with the same name doesn't exist.
wb: Opens a write-only file in binary mode.
w+: Opens a file for writing and reading.
wb+: Opens a file for writing and reading in binary mode.
a: Opens a file for appending new information to it. The pointer is placed at the end of the file. A new file is created if one with the same name doesn't exist.
ab: Opens a file for appending in binary mode.
a+: Opens a file for both appending and reading.
ab+: Opens a file for both appending and reading in binary mode."""
