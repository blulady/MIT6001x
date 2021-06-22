# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 13:48:06 2021

@author: Sarah
"""

s = 'abcdefghijklmnopqrstuvwxyz'
tempst = ''
longest = ''
for i in range(len(s)-1):
    if s[i] <= s[i+1]:
        tempst += s[i]
    elif s[i] >s[i-1] and s[i] > s[i + 1] :
        tempst += s[i]
        if len(tempst) > len(longest):
            longest = tempst
        tempst = ''
    elif s[i] > s[i+1]:
        if len(tempst) > len(longest):
            longest = tempst
        tempst = ''
if longest == '':
    longest = tempst
print(longest)

#s = 'eozlpcdfr'
#s = 'uuemekgvha'
# s = 'lyjmjinjgkkx'
# tempst = ''
# longest = ''
# for i in range(len(s)-1):
#     if s[i] <= s[i+1]:
#         tempst += s[i]
#     elif s[i] >=s[i-1] and s[i] >= s[i + 1]:
#         tempst += s[i]
#         if len(tempst) > len(longest):
#             longest = tempst
#         tempst = ''
#     elif s[i] >= s[i+1]:
#         if len(tempst) > len(longest):
#             longest = tempst
#         tempst = ''
# if len(tempst) > len(longest):
#     longest = tempst
# if longest == '':
#     longest = tempst
# print(longest)

s = 'lyjmjinjgkkx'
tempst = ''
longest = ''
for i in range(len(s)-1):
    if s[i] <= s[i+1]:
        tempst += s[i]

    elif s[i] >=s[i-1] and s[i] >= s[i + 1]:
        tempst += s[i]
        if len(tempst) > len(longest):
            longest = tempst
        tempst = ''
    elif s[i] >= s[i+1]:
        if len(tempst) > len(longest):
            longest = tempst
        tempst = ''
if s[-1] > s[-2] :
    tempst += s[-1]
if len(tempst) > len(longest):
    longest = tempst
if longest == '':
    longest = tempst
print(longest)
#this one works
tempst = ''
longest = ''
for i in range(len(s)-1):
    if s[i] <= s[i+1]:
        tempst += s[i]

    elif s[i] >=s[i-1] and s[i] >= s[i + 1]:
        tempst += s[i]
        if len(tempst) > len(longest):
            longest = tempst
        tempst = ''
    elif s[i] >= s[i+1]:
        if len(tempst) > len(longest):
            longest = tempst
        tempst = ''
if s[-1] > s[-2] :
    tempst += s[-1]
if len(tempst) > len(longest):
    longest = tempst
if longest == '':
    longest = tempst
print(longest)