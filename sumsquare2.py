#!/usr/bin/python
"""
Question: write a function that squares every digit of a given number

Creator: Jerry Haynes
"""
from functools import reduce
import operator


SumofSquares = ((reduce(operator.add, range(1,11))**2)-reduce((lambda i,y: (i+y**2)),range(1, 10+1)))

print(SumofSquares)