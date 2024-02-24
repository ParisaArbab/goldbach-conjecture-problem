"""
Author: Parisa Arbab
Date: Jan 27 2024
Statement:“I have not given or received any unauthorized assistance on this assignment.”
YouTube Link:https://youtu.be/rEczi5bPL3w

Questions:
• Highlight the main loop in which you iterate over the integers 4 through 100.
• Explain the (nested?) loop in which you find two primes to sum to the integer.
• Show the discovery of prime numbers.  How can you optimize this?
"""
def is_prime(num):
    """
    Check if a number is prime.

    Args:
        num (int): The number to be checked.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def goldbach_conjecture_test():
    """
    Test Goldbach's Conjecture for even integers less than 100.

    Prints out pairs of prime numbers that sum up to each even integer from 4 to 100.
    """
    for num in range(4, 101, 2):
        found = False
        for i in range(2, num // 2 + 1):
            if is_prime(i) and is_prime(num - i):
                print(f"{num} = {i} + {num - i}")#sum up eith current integer(num)
                found = True
                break
        if not found:
            print(f"No two primes found that sum up to {num}")

goldbach_conjecture_test()
