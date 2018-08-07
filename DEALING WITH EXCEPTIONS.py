# -*- coding: utf-8 -*-
"""
Created on Sat Jul 28 05:09:41 2018

@author: Ahmad
"""
#Python code can provide handlers for exceptions
try:
    a = int(input("Tell me one number:"))
    b = int(input("Tell me another number:"))
    print(a/b)
    print ("Okay")
except:
    print("Bug in user input.")
print("Outside")

#exceptions raised by any statement in body of try are
#handled by the except statement and execution continues
#after the body of the except statement