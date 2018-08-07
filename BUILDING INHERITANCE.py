# -*- coding: utf-8 -*-
"""
Created on Sat Aug  4 19:43:38 2018

@author: Ahmad
"""

class MITPerson(Person):
    nextIdNum = 0 # next ID number to assign

    def __init__(self, name):
        Person.__init__(self, name) # initialize Person attributes
        self.idNum = MITPerson.nextIdNum # MITPerson attribute: unique ID
        MITPerson.nextIdNum += 1
        
    def getIdNum(self):
        return self.idNum
    
    # sorting MIT people uses their ID number, not name!
    def __lt__(self, other):
        return self.idNum < other.idNum
    
    def speak(self, utterance):
        return (self.getLastName() + " says: " + utterance)