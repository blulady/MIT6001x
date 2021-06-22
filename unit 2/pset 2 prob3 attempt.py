# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 12:58:38 2021

@author: Sarah
"""

# annualInterestRate = 0.15
# montlyInterestRate = annualInterestRate/12
# balance =  16768
# highBalance = (balance * annualInterestRate)+ balance
# check = (balance + highBalance)/2
# low = balance/12
# high= ((balance * annualInterestRate)+balance)/12
# monthlyPayment = (low + high)/2
# newBalance = balance
# epsilon = .01



# while newBalance - (monthlyPayment * 12) > epsilon:
#     newBalance = balance
#     monthlyPayment = (low + high)/2
#     if monthlyPayment * 12 > newBalance:
#         high = monthlyPayment
#     if monthlyPayment * 12 < newBalance:
#         low = monthlyPayment
#     monthlyPayment = (low + high)/2
#     for i in range(12):
#         montlyInterestRate = annualInterestRate/12
#         monthlyUnpaidBalance = newBalance - monthlyPayment
#         newBalance = monthlyUnpaidBalance + (monthlyUnpaidBalance * montlyInterestRate)
#         print(newBalance)
# print(round(monthlyPayment,2))
# print(newBalance)

# annualInterestRate = 0.15
# montlyInterestRate = annualInterestRate/12
# balance =  16768
# highBalance = (balance * annualInterestRate)+ balance
# check = (balance + highBalance)/2
# low = balance/12
# high= ((balance * annualInterestRate)+balance)/12
# monthlyPayment = (low + high)/2
# newBalance = balance
# epsilon = .01



# #while highBalance - (monthlyPayment * 12) > epsilon:
# while newBalance != 0:
#     newBalance = balance
#     monthlyPayment = (low + high)/2
#     if monthlyPayment * 12 > newBalance:
#         high = monthlyPayment
#     if monthlyPayment * 12 < newBalance:
#         low = monthlyPayment
#     monthlyPayment = (low + high)/2
#     for i in range(12):
#         montlyInterestRate = annualInterestRate/12
#         monthlyUnpaidBalance = newBalance - monthlyPayment
#         newBalance = monthlyUnpaidBalance + (monthlyUnpaidBalance * montlyInterestRate)
#         print(newBalance)
# print(round(monthlyPayment,2))
# print(newBalance)

annualInterestRate = 0.15
montlyInterestRate = annualInterestRate/12
balance =  16768
highBalance = (balance * annualInterestRate)+ balance
check = (balance + highBalance)/2
low = balance/12
high= ((balance * annualInterestRate)+balance)/12
monthlyPayment = (low + high)/2
newBalance = balance
epsilon = .01



while newBalance - (monthlyPayment * 12) > epsilon:
    newBalance = balance
    monthlyPayment = (low + high)/2
    if monthlyPayment * 12 > newBalance:
        high = monthlyPayment
    if monthlyPayment * 12 < newBalance:
        low = monthlyPayment
    monthlyPayment = (low + high)/2
    for i in range(12):
        montlyInterestRate = annualInterestRate/12
        monthlyUnpaidBalance = newBalance - monthlyPayment
        newBalance = monthlyUnpaidBalance + (monthlyUnpaidBalance * montlyInterestRate)
        print(newBalance)
print(round(monthlyPayment,2))
print(newBalance)

while newBalance >= 0:
    newBalance = balance
    monthlyPayment = (low + high)/2
    