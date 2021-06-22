# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 10:02:15 2021

@author: Sarah
"""

def printname(firstName, lastName, reverse):
    if reverse:
        print(lastName + ', '+ firstName)
    else:
        print(firstName, lastName)
        
        
def printname2(firstName, lastName, awesome):
    if awesome:
        print(lastName + ', '+ firstName)
    else:
        print(firstName, lastName)
        