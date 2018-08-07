# -*- coding: utf-8 -*-
"""
Created on Sat Jul  7 02:18:51 2018

@author: Ahmad
"""

cube = 27
epsilon = 0.01
num_guesses = 0
low = 1
high = cube
guess = (high + low)/2.0
while abs(guess**3 - cube) >= epsilon:
    if guess**3 < cube :
        low = guess
    else:
        high = guess
    guess = (high + low)/2.0
    num_guesses += 1
print('num_guesses =', num_guesses)
print(guess, 'is close to the cube root of', cube)