#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@author: jerryhaynes
"""

x=0
y=0
def combo():
    global x
    global y
    squredsum = []
    for n in range(2,x+1):
        for y in range(2,y+1):
            squredsum.append(n**y)

    for a in squredsum:
        if squredsum.count(a) >= 2:
            print("remove: ", a)
            squredsum.remove(a)

    squredsum = sorted(squredsum)
    print(squredsum)
    print("The distinct numbers are:", len(squredsum))

def get_x():
    print("Enter number for x:")
    return int(input())
def get_y():
    print("Enter number for y:")
    return int(input())
def getvalues():
    global x,y
    value = True
    while value:
        try:
            x = get_x()
            y = get_y()
            value = False
        except ValueError:
            print("Enter another value:")

getvalues()
combo()