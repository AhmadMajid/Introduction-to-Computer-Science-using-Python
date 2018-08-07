# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 18:54:31 2018

@author: Ahmad
"""

def fib_efficient(n, d):
    if n in d:
        return d[n]
    else:
        ans = fib_efficient(n-1, d) + fib_efficient(n-2, d)
        d[n] = ans
        return ans

d = {1:1, 2:2}
print(fib_efficient(6, d))

#do a lookup first in case already calculated the value
#modify dictionary as progress through function calls
