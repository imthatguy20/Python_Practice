#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 22:10:20 2018

@author: jerryhaynes
"""

def book(checkbooked):
   if len(checkbooked) == 0:
       print("no one has read this.")
   elif len(checkbooked) == 1:
       print(checkbooked[0], "has read this.")
   elif len(checkbooked) == 2:
       print("" + checkbooked[0] + " and " + checkbooked[1], "has read this.")
   elif len(checkbooked) == 3:
       print("" + checkbooked[0] + ", " + checkbooked[1] + "and " + checkbooked[2], "have read this.")
   else:
       print(checkbooked[0] + "," , checkbooked[1], "and", len(checkbooked)-2, "others have read this.")

listing = []
book(listing)
listing = ["Ashley"]
book(listing)
listing = ["Ashley", "Bobby"]
book(listing)
listing = ["Ashley", "Bobby", "Kevin"]
book(listing)
listing = ["Ashley", "Bobby", "Kevin", "Max"]
book(listing)
listing = ["Ashley", "Bobby", "Kevin", "Max", "John"]

