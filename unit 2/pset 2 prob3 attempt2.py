# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 16:24:12 2021

@author: Sarah
"""

annualInterestRate = 0.15
#montlyInterestRate = annualInterestRate/12
balance =  16768
low = balance/12
high= ((balance * annualInterestRate)+balance)/12
newBalance = balance
epsilon = .01


# while newBalance > epsilon:
#     monthlyPayment = (low + high)/2
#     if monthlyPayment * 12 > newBalance:
#         high = monthlyPayment
#     if monthlyPayment * 12 < newBalance:
#         low = monthlyPayment
# #    monthlyPayment = (low/high)/2
#     for i in range(12):
#         montlyInterestRate = annualInterestRate/12
#         monthlyUnpaidBalance = newBalance - monthlyPayment
#         newBalance = monthlyUnpaidBalance + (monthlyUnpaidBalance * montlyInterestRate)
#         print(newBalance)
# print(round(monthlyPayment,2))
# print(newBalance)

while newBalance > 0 < .02:
    monthlyPayment = (low + high)/2
    if monthlyPayment * 12 > newBalance:
        high = monthlyPayment
    if monthlyPayment * 12 < newBalance:
        low = monthlyPayment
#    monthlyPayment = (low/high)/2
    for i in range(12):
        montlyInterestRate = annualInterestRate/12
        monthlyUnpaidBalance = newBalance - monthlyPayment
        newBalance = monthlyUnpaidBalance + (monthlyUnpaidBalance * montlyInterestRate)
        print(newBalance)
print(round(monthlyPayment,2))
print(newBalance)




# monthlyPayment = (low + high)/2

# while (monthlyPayment * 12) - newBalance > epsilon:
#     monthlyPayment = (low + high)/2
#     high = monthlyPayment
#     monthlyPayment = (low + high)/2
#     for i in range(12):
#         monthlyInterestRate = annualInterestRate/12
#         monthlyUnpaidBalance = newBalance - monthlyPayment
#         newBalance = monthlyUnpaidBalance + (monthlyUnpaidBalance * montlyInterestRate)
        
# print(round(monthlyPayment, 2))