# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 09:47:07 2021

@author: Sarah
"""

# s = 'abcbcd'
# tempst = ''
# longest = ''
# for i in range(len(s)-1):
#     if s[i] < s[i+1]:
#         tempst += s[i]
#     elif s[i] >s[i-1] and s[i] > s[i + 1] :
#         tempst += s[i]
#         if tempst > longest:
#             longest = tempst
#             tempst = ''
# print(longest)

# s = 'azcbobobegghakl'
# tempst = ''
# longest = ''
# for i in range(len(s)-1):
#     if s[i] <= s[i+1]:
#         tempst += s[i]
#     elif s[i] >s[i-1] and s[i] > s[i + 1] :
#         tempst += s[i]
#         if tempst > longest:
#             longest = tempst
#             tempst = ''
# print(longest)

# s = 'azcbobobegghakl'
# tempst = ''
# longest = ''
# for i in range(len(s)-1):
#     if s[i] <= s[i+1]:
#         tempst += s[i]
#     elif s[i] >s[i-1] and s[i] > s[i + 1] :
#         tempst += s[i]
#         if tempst > longest:
#             longest = tempst
#         tempst = ''
# print(longest)

# s = 'azcbobobegghakl'
# tempst = ''
# longest = ''
# for i in range(len(s)-1):
#     if s[i] <= s[i+1]:
#         tempst += s[i]
#     elif s[i] >s[i-1] and s[i] > s[i + 1] :
#         tempst += s[i]
#         if tempst > longest:
#             longest = tempst
#             tempst = ''
#     elif s[i] > s[i + 1]:
#         if len(tempst) > len(longest):
#             longest = tempst
#             tempst = ''
# print(longest)

# s = 'azcbobobegghakl'
# tempst = ''
# longest = ''
# for i in range(len(s)-1):
#     if s[i] <= s[i+1]:
#         tempst += s[i]
#     elif s[i] >s[i-1] and s[i] > s[i + 1] :
#         tempst += s[i]
#         if len(tempst) > len(longest):
#             longest = tempst
#         tempst = ''
# print(longest)

#s = 'abcdefghijklmnopqrstuvwxyz'
#s = 'azcbobobegghakl' this code passes this
s = 'azcbobobegghakl'
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
        
print(longest)

s = 'nnfreclxkeblrjvpkaln'
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
        if tempst > longest:
            longest = tempst
        tempst = ''
        
print(longest)

s = 'atufrjvtaoczzcfpb'
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
        if tempst > longest:
            longest = tempst
        tempst = ''
        
print(longest)

        