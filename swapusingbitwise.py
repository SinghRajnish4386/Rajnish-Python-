a=int(input("Enter 1st number:"))
b=int(input("Enter 2nd number:"))
print("before swapping")
print("a=",a,"b=",b)
a=a^b
b=a^b
a=a^b
print("after swapping")
print("a=",a,"b=",b)