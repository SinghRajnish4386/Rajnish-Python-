n=int(input("Enter a Number:"))
for i in range(n):
        for j in range(i):
            print("",end=" ")
        j=-(n-i-1)
        while(j<(n-i)):
          print("*",end=" ")
        j+=1
        print()