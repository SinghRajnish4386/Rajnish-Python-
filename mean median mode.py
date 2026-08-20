import random
import statistics
def generate_random_numbers(n):
    return [random.randint(1, 10) for _ in range(n)]
def calculate_statistics(numbers):
    mean = statistics.mean(numbers)
    median = statistics.median(numbers)
    std_dev = statistics.stdev(numbers)
    return mean, median, std_dev
n = int(input("Enter the number of random numbers: "))
random_numbers = generate_random_numbers(n)
mean, median, std_dev = calculate_statistics(random_numbers)
print(f"Random Numbers: {random_numbers}")
print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Standard Deviation: {std_dev}")
