# -*- coding: utf-8 -*-
"""
Created on Sat Aug  4 14:10:22 2018

@author: Ahmad
"""

class Animal(object):
    def __init__(self, age):
        self.age = age
        self.name = None
        
myanimal = Animal(3)

def get_age(self):
    return self.age
def get_name(self):
    return self.name
def set_age(self, newage):
    self.age = newage
def set_name(self, newname=""):
    self.name = newname
def __str__(self):
    return "animal:"+str(self.name)+":"+str(self.age)