# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 13:48:39 2018

@author: Ahmad
"""
#This gives us another way of generating guesses, which we can check; very efficient

epsilon = 0.01
y = 24.0
guess = y/2.0
numGuesses = 0

while abs(guess*guess - y) >= epsilon:
    numGuesses += 1
    guess = guess - (((guess**2) - y)/(2*guess))
print('numGuesses = ' + str(numGuesses))
print('Square root of ' + str(y) + ' is about ' + str(guess))
