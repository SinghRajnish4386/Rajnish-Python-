def is_palindrome(s):
    """Function to check if a string is a palindrome."""
    s = s.replace(" ", "").lower() 
    return s == s[::-1] 
