a=input("enter a string:")
print(a.replace(a[-1],'*',a.count(a[-1])-1))