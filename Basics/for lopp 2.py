'''n=int(input("Please Enter your value"))
for i in range(1,11,1):
    print(n ,"*",i,"=",i*n)'''

r=int(input("Please Enter row value :"))
c=int(input("Please Enter Column value :"))

'''for i in range(r):
    for j in range(c):
            print("# ",end="")
    print()'''

for i in range(r):
    for j in range(i+1):
            print("# ",end="")
    print()


for i in range(r):
    for j in range(c-i-1):
            print("# ",end="")
    print()