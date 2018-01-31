#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 17:05:25 2018

@author: jerryhaynes
"""
from itertools import cycle
alpha = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,
'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26}

def get_message():
    print("Enter the message that you would like to encrypt:")
    return input()

def get_key():
    key = 0
    while True:
        print("Enter your key:")
        key = int(input())
        return key

def cipher(message,key):
    message = list(message)
    print(message)

    akey = str(key)
    key = []
    for a in akey:
        key.append(int(a))

    loop = cycle(key)
    for item in loop:
        key.append(item)
        if len(key) == len(message):
            break
    i = 0
    final_print = []
    for sumofboth in message:

        final_print.append(key[i] + alpha[sumofboth])
        i += 1

    print(final_print)

m = get_message()
k = get_key()

cipher(m,k)
