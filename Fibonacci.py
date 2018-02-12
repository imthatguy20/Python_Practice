# -*- coding: utf-8 -*-
"""
Each new term in the Fibonacci sequence is generated by adding the previous two
terms. By starting with 1 and 2, the first 10 terms will be:
1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
By considering the terms in the Fibonacci sequence whose values do not exceed four
million, find the sum of the even-valued terms.

"""


total = 0
f1, f2 = 1, 2
while f1 < 4000000:
    if f1 % 2 == 0:
        total = total + f1
        f1, f2 = f2, f1 + f2        #Python supports multiple assignment at once. Right hand side
                                #is fully evaluated before setting the variables.
print(total)

