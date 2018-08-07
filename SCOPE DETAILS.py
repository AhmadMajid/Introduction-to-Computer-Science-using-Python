# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 22:33:05 2018

@author: Ahmad
"""

def g(x):
    def h():
        x = 'abc'
    x = x + 1
    print('in g(x): x ='. x)
    h()
    return x

x = 3

z = g(x)