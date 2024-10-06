#!/usr/bin/env python3
"""
Fibonacci Sequence

Create a program that generates Fibonacci numbers less than a limit and writes them to a file. The _Fibonacci_ sequence is a sequence in which each number is the sum of the two preceding ones: 

`0, 1, 1 (0+1), 2 (1+1), 3 (2+1), 5 (3+2), ...`

	- Use a function to generate Fibonacci numbers as a list
	- Use `with` statements for file operations
	- Handle potential file I/O errors with `try`/`except`
	- Use command-line arguments (via `argparse`) to specify the upper limit and output file name

Task: Generate the Fibonacci numbers less than 100 and write them to `fibonacci_100.txt`
"""
import argparse

def fibonacci(limit):
    fib = []
    x = 0
    y = 1
    
    while x < limit:
        fib.append(x)
        x, y = y, x + y
    return fib

def write_to_file(fib, file_name):
     try:
          with open(file_name, "w") as f:
                for number in fib:
                       f.write(f"{number}\n")
     except: 
          print("File I/O error")

def main():
    parser = argparse.ArgumentParser(description="Generate Fibonacci numbers less than a limit.")
    parser.add_argument("limit", type = int, help="Upper limit for Fibonacci numbers")
    parser.add_argument("output_file", type = str, help="Output file name")

    args = parser.parse_args()
    fib = fibonacci(args.limit)
    write_to_file(fib, args.output_file)

if __name__ == "__main__":
    main()