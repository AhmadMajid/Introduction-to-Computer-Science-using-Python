# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 18:38:29 2018

@author: Ahmad
"""

def most_common_words(freqs):
    values = freqs.values()
    best = max(values)
    words = []
    for k in freqs:
        if freqs[k] == best:
            words.append(k)
    return (words, best)