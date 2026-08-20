n=int(input("enter a number:"))
m=n
k=n
t=n
s1=0
s2=0
while(m!=0):
    p=m%10
    s1=s1+1
    m=m//10
    while(1):
        if(t==0):
            break
        b=t%10
        s2=s2+b**s1
        t=t//10
        if(s2==k):
            print("it is an armstrong")
        else:
            print("it is not an armstrong")