prime=0
comp=0
while True:
    n=int(input("Enter any number(-1 to exit):"))
    if(n==-1):
        break
    else:
        is_prime=True
        for i in range(2,n):
            if(n%i==0):
                is_prime=False
                break
            if is_prime:
             prime+=1
            else:
                comp+=1
print("no of prime number=",prime)
print("no of composite number=",comp)