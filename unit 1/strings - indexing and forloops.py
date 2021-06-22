# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 21:32:46 2021

@author: Sarah
"""

x = 5
if x != 5:
    print('i is 5')
else:
    print('i is not 5\n')
    
string = "hello"
for i in range(len(string)-1):
    print(string[i: i+2])



for i in range(len(string)):
    print(string[i: i+2])
    
s = 'azcbobobegghakl'
new = ''
longest = ''
for i in range(len(s)-1):
    if s[i] <= s[i+1]:
        new += s[i:i+1]
    if new > longest:
        longest = new        
print(longest)

for i in range(len(s)-1):
    if s[i] <= s[i+1]:
        new += s[i:i+2]
    if new > longest:
        longest = new        
print(longest)
 
for i in range(len(s)-1):
    new = ''
    while s[i] <= s[i+1]:
        new += s[i:i+1]
        break
    if new > longest:
        longest = new        
print(longest)

#m is a string
#new is an empty string
#for i in range(len(m)-1):
#    new += str(ord(m[i]))
    
# st = ''
# for i in range(len(s)-1):
#     first = ord(s[i])
#     second = ord(s[i+1])
#     if second > first:
#         st += s[i]
#         st += s[i+1]
# print(st)

# st2 = ''
# for i in range(len(s)-1):
#     if s[i] < s[i+1]:
#         mestr = ''
#         while True:
#             mestr += s[i]
#             mestr += s[i+1]
#         if mestr > st2:
#             st2 = mestr
# print(mestr)


# s = 'azcbobobegghakl'


for i in range(len(s)-1):
    new = ''
    if s[i] <= s[i+1]:
        new += s[i]
    if len(new) > len(longest):
        longest = new        
print(longest)

# for i in range(len(s)-1):
#     new = ''
#     if s[i] <= s[i+1]:
#         while True:
#             new += s[i]
#     if len(new) > len(longest):
#         longest = new        
# print(longest)

s = 'abcbcd'
longlist = ''
emptylist = ''
for i in range(len(s)-1):
    if s[i] <= s[i+1]:
        emptylist += s[i]
    if s[i] > s[i+1] and s[i-1] < s[i]:
        emptylist += s[i]
    if len(emptylist) > len(longlist):
        longlist = emptylist
        emptylist = ''
print(longlist)
        
    