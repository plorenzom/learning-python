"""Fibonacci series implementation."""

import argparse

def calculate(number):
    """Calculate Fibonacci series up to number."""

    fibonacciSeries = []
    precedingOne, precedingTwo = 0, 1

    while (precedingOne < number):
        fibonacciSeries.append(precedingOne)
        precedingOne, precedingTwo = precedingTwo, (precedingOne + precedingTwo)
    
    return fibonacciSeries

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("number", help = "calculate Fibonacci series up to number", type = int)
    args = parser.parse_args()
    fibonacciSeries = calculate(args.number)
    print(fibonacciSeries)

if (__name__ == "__main__"):
    main()