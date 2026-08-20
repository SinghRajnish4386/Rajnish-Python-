n=0
m=1
c=0
while n<=100:
    s=n+m
    n=m
    m=s
    if(s%2!=0):
        continue
    c=c+s
print("sum of even number of fibonacci series",c)
