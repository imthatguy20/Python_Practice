#!/usr/bin/python
"""
Question: write a function that squares every digit of a given number

Creator: Jerry Haynes
"""

def squareofthesum(n):
    return sum(range(1, n+1)) ** 2

def square(x,y):
    return x**y

SumofSquares = map((lambda i: i**2),range(1, 11))
#SquareSum = map((lambda i: (i+0)), (range(1, 10)))
#sum1 = (map(square, range(1,11)(range(1, 11)**2)))
#print(sum1)

print(squareofthesum(10) - sum(SumofSquares))

