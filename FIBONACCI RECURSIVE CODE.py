# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 18:51:02 2018

@author: Ahmad
"""

def fib(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return fib(n-1) + fib(n-2)
#two base cases
#calls itself twice
#this code is inefficient