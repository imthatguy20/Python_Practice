#!/usr/bin/python
"""
Question: write a function that squares every digit of a given number

Creator: Jerry Haynes
"""
def sumofsquares(n):
    return sum(i**2 for i in range(1, n+1))

def squareofthesum(n):
    return sum(range(1, n+1)) ** 2

print(squareofthesum(10) - sumofsquares(10))

