# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 17:33:59 2021

@author: Tan Say Yen
"""

import numpy

def polysum (n , s):
    ### n is the number of sides of the polygon
    ### s is the length of each side
    ### polysum returns the sum of the area and square of the perimeter
    pi = numpy.pi
    area = (0.25*n*s**2)/numpy.tan(pi/n)
    perimeter = n*s
    
    answer = round(area + perimeter**2,4)
    
    return answer