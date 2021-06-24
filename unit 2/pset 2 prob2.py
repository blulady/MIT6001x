# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 08:40:57 2021

@author: Sarah
"""
annualInterestRate = 0.2
#montlyInterestRate = annualInterestRate/12
balance = 3926
monthlyPayment = 10 
newBalance = balance
#months = 0

while newBalance > 0:
    newBalance = balance
    monthlyPayment += 10
    for i in range(12):
        montlyInterestRate = annualInterestRate/12
        monthlyUnpaidBalance = newBalance - monthlyPayment
        newBalance = monthlyUnpaidBalance + (monthlyUnpaidBalance * montlyInterestRate)

# #answer for problem 3
# annualInterestRate = 0.2
# #montlyInterestRate = annualInterestRate/12
# balance = 3926
# monthlyPayment = 200
# newBalance = balance

# while newBalance > 0 < .2:
#     newBalance = balance
#     monthlyPayment += .1
#     for i in range(12):
#         montlyInterestRate = annualInterestRate/12
#         monthlyUnpaidBalance = newBalance - monthlyPayment
#         newBalance = monthlyUnpaidBalance + (monthlyUnpaidBalance * montlyInterestRate)
        



    