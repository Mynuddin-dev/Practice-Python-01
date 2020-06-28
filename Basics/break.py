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
