# -*- coding: utf-8 -*-
"""
input: two integers, n: the number of sides a polygon has
s: the length of a single side
output: a single integer (rounded to 4 digits) that is the sum of the 
area and squared parimeter
"""

from math import *

def polysum(n,s):
    area = (.25*n*s**2)/(tan(pi/n))
    perimeter = n*s
    return round(area + perimeter**2, 4)