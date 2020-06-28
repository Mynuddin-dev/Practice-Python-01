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