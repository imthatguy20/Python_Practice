#!/usr/bin/python
"""

Creator: Jerry Haynes
"""
import random
compass = ['N', 'S', 'E', 'W']           # a sequence or set will work here.
startingpoint = []
n=0
e=0
s=0
w=0

def routebacktostart(start,i):
    global n,e,s,w
    if start == 'N':
        n+=1
        print("Path Going North")
    elif start == 'E':
        e+=1
        print("Path going East")
    elif start == 'S':
        s+=1
        print("Path going South")
    elif start == 'W':
        w+=1
        print("Path going West")
    else:
        print("no path found")

def path():
    var = False
    print("Enter The Path you would like to go:")
    home = [str(x) for x in input().split()]
    [home.append(random.choice(compass)) for i in range(0,10)]
    [routebacktostart(home[i],i) for i in range(0,len(home))]
    print(home)
    print("N:",n,"  E:",e,"  S:",s,"  W:",w)
    if len(home) == 10 and ((n-s) == 0 or (s-n) == 0) and ((w-e) == 0 or (e-w) == 0):
        var = True
    return var

def main():
    location = path()
    if location:
        print("Trip only took 10 minutes", location)
    else:
        print("Trip took more than 10 minutes", location)
main()
