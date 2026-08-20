p=float(input("principle="))
r=0
t=float(input("time="))
if p<200000:
    r=10
elif p>=200000 and p<1000000:
    r=12
elif p>=1000000:
    r=15
else:
    print("something went wrong!!")
print("SI=",(p*r*t)/100)