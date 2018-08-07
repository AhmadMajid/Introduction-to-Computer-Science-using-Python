# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 22:21:19 2018

@author: Ahmad
"""

#arguments can take on any type, even functions

def func(a)():
    print('inside func_a')
def func(b)(y):
    print('inside func_b')
    return y
def func_c(z):
    print('inside func_c')
    return z()
print(func_a())
print(5 + func_b(2))
print(func_c(func_a))