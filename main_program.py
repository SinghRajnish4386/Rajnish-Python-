# main_program.py
from factorial_module import factorial
num = int(input("Enter a number to find its factorial: "))
result = factorial(num)
print(f"The factorial of {num} is: {result}")
