num1=int(input("num1="))
num2=int(input("num2="))
num3=int(input("num3="))
num4=0
if num1<num2:
    num1,num2=num2,num1
if num1<num3:
    num1,num3=num3,num1
if num2<num3:
    num2,num3=num3,num2
print(num1,">",num2,">",num3,">")
