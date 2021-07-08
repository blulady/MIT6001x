# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 13:38:50 2021

@author: Sarah
"""

def findExtremeDivisors(n1, n2):
    """ Assumes n1 & n2 are positive ints
    returns a tuple containing the smallest common divisor > 1 and 
    the largest common divisor of n1 and n2. If no common divisor,
    returns (None, None)"""
    minVal, maxVal = None, None 
    for i in range(2, min(n1, n2) +1):
        if n1%i == 0 and n2%i == 0:
            if minVal == None:
                minVal = i
            maxVal = i
    return(minVal, maxVal)

monthNumbers = {'Jan':1, 'Feb':2, 'Mar':3, 'Apr':4,
'May':5, 1:'Jan', 2:'Feb', 3:'Mar', 4:'Apr', 5:'May'}

print('The third month is ' + monthNumbers[3]) dist = monthNumbers['Apr'] - monthNumbers['Jan']