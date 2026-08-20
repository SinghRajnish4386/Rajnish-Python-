from prime_module import is_prime
def find_primes_in_range(start, end):
    prime_numbers = []
    for num in range(start, end + 1):
        if is_prime(num):
            prime_numbers.append(num)
    return prime_numbers
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))
primes = find_primes_in_range(start, end)
if primes:
    print(f"Prime numbers between {start} and {end} are: {primes}")
else:
    print(f"There are no prime numbers between {start} and {end}.")
