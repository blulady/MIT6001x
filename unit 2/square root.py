# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 11:42:10 2021

@author: Sarah
"""

ans = 0
neg_flag = False
x = int(input("Enter an integer: "))
if x < 0:
    neg_flag = True
while ans**2 < x:
    ans = ans + 1
if ans**2 == x:
    print("Square root of", x, "is", ans)
else:
    print(x, "is not a perfect square")
    if neg_flag:
        print('Just Checking... did you mean', str(-x) + "?")