# -*- coding: utf-8 -*-
"""
Created on Sat Aug  4 14:10:22 2018

@author: Ahmad
"""

class Animal(object):
    def __init__(self, age):
        self.age = age
        self.name = None
        
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

class Cat(Animal):
    def speak(self):
        print("meow")
    def __str__(self):
        return "cat:"+str(self.name)+":"+str(self.age)
#add new functionality with speak()
#   instance of type Cat can be called with new methods
#   instance of type Animal throw error if called with new methods

#__init__ is not missing, uses the Animal version

class Rabbit(Animal):
    def speak(self):
        print("meep")
    def __str__(self):
        return "rabbit:"+str(self.name)+":"+str(self.age)