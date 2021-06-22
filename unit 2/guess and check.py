# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 08:40:31 2021

@author: Sarah
"""

cube = 8
#cube = 28 #doesn't print anything, not a perfect cube

for guess in range(cube):
    if guess**3 == cube:
        print('Cube root of', cube, "is", guess)
        
for guess in range(abs(cube)+1):
    if guess**3 == abs(cube):
        break
if guess**3 != abs(cube):
    print(cube, "is not a perfect cube")
else:
    if cube < 0:
        guess = -guess
    print("cube root of " + str(cube) + ' is ' + str(guess))