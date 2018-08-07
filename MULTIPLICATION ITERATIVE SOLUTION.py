# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 00:56:44 2018

@author: Ahmad
"""

#"multiply a * b" is equivalent to "add a to itself b times"
#capture state by
#   an interation number(i) starts at b
#       i <- i-1 and stop at 0
#   a current value of computation(result)
#       result <- result + a

def mult_iter(a, b):
    result = 0
    while b > 0:
        result += a
        b -= 1
    return result