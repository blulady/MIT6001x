# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 15:23:03 2021

@author: Sarah
"""

def g(x):
    def h():
        x = 'abc'
    x = x + 1
    print('in g(x): x -', x)
    h()
    return x

x = 12
