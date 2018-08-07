# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 14:08:17 2018

@author: Ahmad
"""

def mult(a, b):
    if b == 1:
        return a
else:
    return a + mult(a, b-1)