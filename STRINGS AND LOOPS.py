# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 19:15:10 2018

@author: Ahmad
"""
s = "abcdefgh"
for index in range(len(s)):
    if s[index] == 'i' or s[index] == 'u':
        print("There is an i or u")
        
for char in s:
    if char == 'i' or char == 'u':
        print("There is an i or u")
