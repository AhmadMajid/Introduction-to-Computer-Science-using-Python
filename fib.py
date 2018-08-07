# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 17:28:20 2018

@author: Ahmad
"""

def fib(x):
    """assumes x an int >= 0
        returns Fibonacci of x"""
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x-1) + fib(x-2)