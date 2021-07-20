# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 12:47:50 2021

@author: Sarah
"""

def genPrimes():
    num1 = 2
    num2 = 3
    x = 1
    listoprimes = [2,3,5,7,11,13,17,19,23,29]
    while True:
        x +=1
        if x%2 !=0 and x%3 !=0 and x%5 != 0 and x%7 != 0 and x%11 != 0 and x%13 !=0 and x%17 !=0 and x%19 !=0 and x%23 != 0 and x%29 != 0 or x in listoprimes:
            listoprimes.append(x)
            yield(x)
            

def genPrimes2():
    x = 1
    primelist = [2,3]
    while True:
        for prime in primelist:
            x +=1
            if x%prime != 0 or x in primelist:
                primelist.append(x)
                yield(x)
                
                
def genPrimes():
    x = 1
    primelist = [2,3]
    while True:
        for prime in primelist:
            x +=1
            if x%prime != 0 or x in primelist:
                primelist.append(x)
                yield(x)