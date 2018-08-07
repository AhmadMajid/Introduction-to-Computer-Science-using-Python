# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 17:35:40 2018

@author: Ahmad
"""

def isPalindrome(s):
    
    def toChars(s):
        s = s.lower()
        ans = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                ans = and + c
        return ans
    
    def isPal(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and isPal(s[1:-1])
        
    return isPal(toChars(s))

print("")
print('Is eve a palindrome?')
print(isPalindrome('eve))

print('')
print('Is able was I ere I saw Elba a palindrome?')
print(isPalindrome)('Able was I, ere I saw Elba'))