# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 14:50:05 2018

@author: Ahmad
"""

def applyFuns(L, x):
    for f in L:
        print(f(x))
        
applyFuns([abs, int, fact, fib]), 4)
4
4
24
5