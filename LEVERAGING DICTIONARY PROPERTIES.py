# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 18:42:16 2018

@author: Ahmad
"""

def words often(freqs, minTimes):
    result = []
    done = False
    while not done:
        temp = most_common_words(freqs)
        if temp[1] >= minTimes:
            result.append(temp)
            for w in temp[0]:
                del(freqs[w])
        else:
            done = True
    return result

print(words_often(beatles, 5))