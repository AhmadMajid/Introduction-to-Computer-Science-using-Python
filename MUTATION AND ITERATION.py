# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 14:34:11 2018

@author: Ahmad
"""
#avoid mutating a list as you are iterating over it
#def remove_dups(L1, L2):
#   for e in L1:
#       if e in L2:
#           L1.remove(e)
def remove_dups_new(L1, L2):
    L1_copy = L1[:]
    for e in L1_copy:
        if e in L2:
            L1.remove(e)