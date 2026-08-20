a=int(input("enter the starting range"))
b=int(input("enter the ending range"))
sum=0
for i in range(a,b):
    if(i<2):
        continue
    is_prime=True
    for j in range(2,i):
        if(i%j==0):
            is_prime=False
            break
        if is_prime:
            sum=sum+i
print(sum)