# # -*- coding: utf-8 -*-
# """
# Created on Wed Jun 30 16:09:37 2021

# @author: Sarah
# """

# total = 0
# string = '1.23,2.4,3.123'
# string = string.split(',')
# for c in string:
#     total = total + float(c)
# print(total)

# def isIN(string1, string2):
#     if string1 in string2:
#         return True
#     elif string2 in string1:
#         return True
#     else:
#         return False
    
# def f(x):
#     y = 1
#     x = x + y
#     print('x = ', x)
#     return x

# x = 3
# y = 2
# z = f(x)

# print('z =', z)
# print('x =', x)
# print('y =', y)

def f(x):
    def g():
        x = 'abc'
        print('x =', x)
    def h():
        z = x
        print('z =', z)
    x = x + 1
    print('x =', x)
    h()
    g()
    print('x =', x)
    return g

x = 3
z = f(x)
print('x =', x)
print('z =', z)
z()