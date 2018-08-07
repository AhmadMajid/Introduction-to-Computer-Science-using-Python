# -*- coding: utf-8 -*-
"""
Created on Sat Aug  4 17:30:45 2018

@author: Ahmad
"""

def __add__(self, other):
    # returning object of same type as this class
    return Rabbit(0, self, other)

#define + operator between two Rabbit instances
    #define what something like this does: r4 = r1 + r2
    #where r1 and r2 are Rabbit instances
    #r4 is a new Rabbit instance with age 0
    #r4 has self as one parent and other as the other parent
    #in __init__, should change to check that parent1 and
    #parent2 are of type Rabbit