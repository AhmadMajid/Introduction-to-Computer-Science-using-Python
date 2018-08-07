# -*- coding: utf-8 -*-
"""
Created on Sun Aug  5 02:05:11 2018

@author: Ahmad
"""

class Grades(object):
    """A mapping from students to a list of grades"""
    def __init__(self):
        """Create empty grade book"""
        self.students = []  # list of Student objects
        self.grades = {}    # maps idNum -> list of grades
        self.isSorted = True # true if self.students is sorted

    def addStudent(self, student):
    """Assumes: student is of type Student
        Add student to the grade book"""
        if student in self.students:
            raise ValueError('Duplicate student')
            self.students.append(student)
            self.grades[student.getIdNum()] = []
            self.isSorted = False
    