# Simple Interest Calculator
p = int(input("Enter the principal amount: "))
r = int(input("Enter the rate of interest: "))
t = int(input("Enter the time (in years): "))

si = (p * r * t) / 100
total_amount = si + p

print("Interest =", si)
print("Total amount =", total_amount)
