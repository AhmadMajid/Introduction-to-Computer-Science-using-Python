# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 14:45:14 2018

@author: Ahmad
"""

def applytoEach(L, f):
    """assumes L is a list, f a function mutates L by replacing each element, e, of L by f(e)"""
    for i in range(len(L)):
        L[i] = f(L[i])