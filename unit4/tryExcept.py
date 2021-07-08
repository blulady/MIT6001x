# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 14:51:23 2021

@author: Sarah
"""

# while True:
#     try:
#         n = input("please enter a number ")
#         n = int(n)
#         break 
#     except ValueError:
#         print('input not an integer: try again')
# print("correct input!!")

# while True:
#     try:
#         n = int(input("please enter a number "))
#         break 
#     except ValueError:
#         print('input not an integer: try again')
# print("correct input!!")

# data = []
# file_name = input('Provde a file name ')
# try:
#     fh = open(file_name, 'r')
# except IOError:
#     print('cannot open', file_name)
# else:
#     for new in fh:
#         if new != '\n':
#             addit = new[:-1].split(',')
#             data.append(addit)
#     fh.close()

# def fancy_divide(numbers,index):
#     try:
#         denom = numbers[index]
#         for i in range(len(numbers)):
#             numbers[i] /= denom
#             x = numbers[i] / denom
#             print(x)
#     except IndexError:
#         print("-1")
#     else:
#         print("1")
#     finally:
#         print("0")
        
        
# def fancy_divide(numbers, index):
#     try:
#         denom = numbers[index]
#         for i in range(len(numbers)):
#             numbers[i] /= denom
#     except IndexError:
#         fancy_divide(numbers, len(numbers) - 1)
#     except ZeroDivisionError:
#         print("-2")
#     else:
#         print("1")
#     finally:
#         print("0")

def fancy_divide(list_of_numbers, index):
   denom = list_of_numbers[index]
   return [simple_divide(item, denom) for item in list_of_numbers]


def simple_divide(item, denom):
    try:
        item / denom
    except ZeroDivisionError:
        return 0
    else:
        return item / denom
      
