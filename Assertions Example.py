# -*- coding: utf-8 -*-
"""
Created on Sat Jul 28 10:29:56 2018

@author: Ahmad
"""

def avg(grades):
    assert not len(grades) == 0, 'no grades data'
    return sum(grades)/len(grades)

#raises an AssertionError if it is given an empty list for grades
#otherwise runs ok