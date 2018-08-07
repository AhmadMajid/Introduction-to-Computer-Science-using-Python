# -*- coding: utf-8 -*-
"""
Created on Sun Jul  1 13:36:07 2018

@author: Ahmad
"""

mysum = 0
for i in range(5, 11, 2):
    mysum += i
    if mysum == 5:
        break
print(mysum)