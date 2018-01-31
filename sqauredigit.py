#!/usr/bin/python
"""
Question: write a function that squares every digit of a given number

Creator: Jerry Haynes
"""

def squaredigit(number):
    try:
        return int(''.join((str(int(w) ** 2) for w in str(int(number)))))
    except ValueError:
        return 0


print(squaredigit(2476))