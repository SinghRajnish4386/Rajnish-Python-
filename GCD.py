a=int(input("Enter a number:"))
b=int(input("Enter b number:"))
if(b>a):
    print("yes")
    temp=a
    a=b
    b=temp
print(a,b)
r=b
while(r>0):
    r=a%b
    if(r==0):
        print(b,"is GCD")
        break
    else:
        a=b
        b=r