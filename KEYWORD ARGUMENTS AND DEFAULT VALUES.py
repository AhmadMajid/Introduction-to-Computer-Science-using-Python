# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 22:57:17 2018

@author: Ahmad
"""

#Simple function definition, if last argument is TRUE,
#then print lastName, firstName, else firstName,
#lastName

def printName(firstName, lastName, reverse):
    if reverse:
        print(lastName + ', ' + firstName)
    else:
        print(firstName, lastName)