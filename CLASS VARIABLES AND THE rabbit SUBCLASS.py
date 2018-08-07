# -*- coding: utf-8 -*-
"""
Created on Sat Aug  4 16:31:28 2018

@author: Ahmad
"""

#subclasses inherit all data attributes and methods of the parent class

class Rabbit(Animal):
    tag = 2
    def __init__(self, age, parent1=None, parent2=None):
        Animal.__init__(self, age)
        self.parent1 = parent1
        self.parent2 = parent2
        self.rid = Rabbit.tag
        Rabbit.tag += 1
#tag used to give unique id to each new rabbit instance
        
        
        
        