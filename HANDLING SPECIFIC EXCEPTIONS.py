# -*- coding: utf-8 -*-
"""
Created on Sat Jul 28 05:13:33 2018

@author: Ahmad
"""
#have separate except cluases to deal with a particular
#type of exception
try:
    a = int(input("Tell me one number: "))
    b = int(input("Tell me another number: "))
    print("a/b = ", a/b)
    print("a+b = ", a+b)
except ValueError:
    print("Could not convert to a number.")
except ZeroDivisionError:
    print("Can't divide by zero")
except:
    print("Something went very wrong.")