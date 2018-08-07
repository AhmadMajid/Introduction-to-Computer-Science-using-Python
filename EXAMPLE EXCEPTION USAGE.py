# -*- coding: utf-8 -*-
"""
Created on Sat Jul 28 05:23:20 2018

@author: Ahmad
"""

while True:
    try:
        n = input("Please enter an integer: ")
        n = int(n)
        break
    except ValueError:
        print("Input not an integer; try again")
print("Correct input of an integer!")