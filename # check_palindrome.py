# check_palindrome.py
from palindrome_module import is_palindrome
user_input = input("Enter a string to check if it's a palindrome: ")
if is_palindrome(user_input):
    print(f"'{user_input}' is a palindrome.")
else:
    print(f"'{user_input}' is not a palindrome.")