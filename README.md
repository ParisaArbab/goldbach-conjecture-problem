# goldbach-conjecture-problem
 This Python code tests Goldbach's Conjecture for even numbers less than 100, demonstrating that each can be expressed as the sum of two prime numbers.
This Python code tests Goldbach's Conjecture for even numbers less than 100, demonstrating that each can be expressed as the sum of two prime numbers.

The is_prime function checks if a number is prime, considering numbers less than 2 as non-prime, directly confirming 2 and 3 as prime, and efficiently testing divisibility for larger numbers to avoid unnecessary calculations.

The goldbach_conjecture_test function iterates through even numbers from 4 to 100, searching for two prime numbers that add up to each. It prints the pairs of prime numbers for each even number, confirming the conjecture for numbers in this range. If no prime pair is found for an even number, which doesn't happen within the tested range, it would notify of the failure (though the code is structured in a way that it expects to always find such a pair, aligning with the conjecture's claim).
