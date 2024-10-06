#!/usr/bin/env python3
"""
Largest Prime Fibonacci Number

Write a program that takes a number as an argument, finds the *Fibonacci* numbers less than that number, and prints the largest prime number in the list. 

	- Use command-line arguments to specify the upper limit 
	- Implement a function to check if a number is prime
	- Import and use the Fibonacci generating function from problem 1 as a module

Task: Find the largest prime Fibonacci number less that 50000
"""

import argparse
from fibonnaci import fibonacci

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    else:
        return True

def big_prime_fib(limit):
    fib_num = fibonacci(limit)  
    primes = [num for num in fib_num if is_prime(num)]
    if primes: 
        return max(primes)

def main():
    parser = argparse.ArgumentParser(description= "Find largest prime Fibonacci number")
    parser.add_argument("limit", type = int, help = "Upper limit for Fibonacci sequence")
    
    args = parser.parse_args()
    
    largest_prime = big_prime_fib(args.limit)
    
    print(largest_prime)
    

if __name__ == "__main__":
    main()


# the largest prime fibonacci sequence number below 50,000 is 28,657
 