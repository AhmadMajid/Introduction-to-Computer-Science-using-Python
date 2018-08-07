# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 21:56:56 2018

@author: Ahmad
"""
#formal parameter gets bound to the value of
#actual parameter when function is called

#new scope/frame/environment created when enter a function

#scope is mapping of names to objects

def f( x ):
    x = x + 1
    print('in f(x): x =', x)
    return x
x = 3
z = f( x )