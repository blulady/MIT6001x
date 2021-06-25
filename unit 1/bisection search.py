# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 11:29:14 2021

@author: Sarah
"""

x = 25
epsilon = .01
numGuesses = 0
low = 1.0
high = x

ans = (high + low)/2

while abs(ans**2 - x) >= epsilon:
    print('low = ' + str(low) + 'high = ' + str(high))
    numGuesses += 1
    if ans**2 < x:
        low = ans 
    if ans**2 > x:
        high = ans 
    ans =(high + low)/2
print('numGuesses = ' + str(numGuesses))
print(str(ans) + 'is close to square root of ' + str(x))