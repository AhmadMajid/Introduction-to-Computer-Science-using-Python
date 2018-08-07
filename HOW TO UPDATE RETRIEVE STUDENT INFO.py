# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 15:35:18 2018

@author: Ahmad
"""

def get_grade(student, name_list, grade_list, course_list):
    i = name_list.index(student)
    grade = grade_list[i]
    course = course_list[i]
    return (course, grade)

#messy if have a lot of different info to keep track of
#must maintain many lists and pass them as arguments
#must always index using integers
#must remember to change multiple lists