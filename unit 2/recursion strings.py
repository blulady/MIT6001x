# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 11:37:00 2021

@author: Sarah
"""


def isIn1(char, aStr):
        
    charCompare = ''
    while charCompare != char:
        length = len(aStr)
        charCompareIndex = (length//2) -1
        charCompare = aStr[charCompareIndex]
        if charCompare == char:
            return True
        if charCompare < char:
            aStr = aStr[charCompareIndex:]
        elif charCompare > char:
            aStr = aStr[:charCompareIndex]
            
            
def isIn(char, aStr):
    if aStr == char:
        return True
    if aStr == '':
        return False
    if len(aStr) == 1 and aStr != char:
        return False
    length = len(aStr)
    charCompareIndex = (length//2)
    charCompare = aStr[charCompareIndex]
    if charCompare == char:
        return True
    elif charCompare < char:
        return isIn(char, aStr[charCompareIndex:])
    elif charCompare > char:
            return isIn(char, aStr[:charCompareIndex])
        
    
    
    