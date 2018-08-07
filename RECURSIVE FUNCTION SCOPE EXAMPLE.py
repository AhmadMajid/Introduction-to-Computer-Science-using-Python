# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 14:15:13 2018

@author: Ahmad
"""

def fact(n):
    if n == 1:
        return 1
    else:
        return n*fact(n-1)

print(fact(4))