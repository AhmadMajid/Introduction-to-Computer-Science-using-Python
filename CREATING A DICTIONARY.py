# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 17:04:57 2018

@author: Ahmad
"""

def lyrics_to_frequencies(lyrics):
    myDict = {}
    for word in lyrics:
        if word in myDict:
            myDict[word] += 1
        else:
            myDict[word] = 1
    return myDict