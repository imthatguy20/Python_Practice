#!/usr/bin/python
"""
Question:
Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).

Creator: Jerry Haynes
"""

l = [] # Creates a list of numbers
for i in range(2000, 3200): #sets a range between 2000 and 3200
    if(i%7 == 0) and (i%5 != 0): # == is comparing
        l.append(str(i)) # append is used to add on a element
    print(';'.join(l)) # This method joins together methods

