# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 13:06:12 2021

@author: Sarah
"""

def mult(a,b):
    if b == 1:
        return a
    else:
        return a + mult(a, b-1)
    
def factorial(n):
    if n ==1:
        return
    else:
        return n*factorial(n-1)
    
def factorial_iter(n):
    prod = 1
    for i in range(1, n+1):
        prod *= i
    return prod


# def iterPower(base, exp):
#     prod = 1
#     for i in range(1, exp+1):
#         prod = base * base
#     return prod

# def iterPower2(base, exp):
#     prod = base
#     for i in range(1, exp+1):
#         prod = base * base
#     return prod

#this is the one that works

def iterPower3(base, exp):
    prod = 1
    for i in range(1, exp+1):
        prod = prod * base
    return prod
        
"""A good way to think about recursion is that 
recursion is the process of solving a given problem 
with a smaller instance of the same problem.

So, how could we express base**exp as a smaller instance of an
 exponential equation?
 base = base*base**exp-1"""
 
def recurPower(base, exp):
    if exp == 1:
        return base
    else:
        return base * recurPower(base, exp-1)
    
def gcdIter(a, b):
    c = 0
    d = []
    if a >= b:
        c = a
    else:
        a < b
        c = b
    for i in range(1, c+1):
        if a% i == 0 and b% i== 0:
            d.append(i)
    return max(d)
            
def gcdIter2(a, b):
    c = 0
    if a >= b:
        c = b
    else:
        a < b
        c = a
    for i in range(c, 1, -1):
        if a% i == 0 and b% i== 0:
            print(i)

def gcdIter3(a, b):
    start = min(a,b)
    for i in range(start, 1, -1):
        if a% i == 0 and b% i== 0:
            print(i)
            
def gcdRecur(a,b):
    if b == 0:
        return a
    else:
        return gcdRecur(b, a % b)
#return a + mult(a, b-1)
        