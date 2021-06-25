# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 11:00:06 2021

@author: Sarah
"""

# annualInterestRate = 0.15
# balance =  16768
# high= ((balance * annualInterestRate)+balance)/12
# low = balance/12
# newBalance = balance
# endBalance = balance
# epsilon = .02

# while endBalance > epsilon:
#     newBalance = balance
#     monthlyPayment = (low + high)/2
#     if endBalance > 0 and endBalance < .2:
#         print(round(monthlyPayment, 2))
#         break
#     elif endBalance > 0:
#         high = monthlyPayment
#     elif endBalance < 0:
#         low = monthlyPayment
#     for i in range(12):
#         montlyInterestRate = annualInterestRate/12
#         monthlyUnpaidBalance = newBalance - monthlyPayment
#         newBalance = monthlyUnpaidBalance + (monthlyUnpaidBalance * montlyInterestRate)
#         endBalance = newBalance
#     print(round(monthlyPayment, 2))
    
        
        
# annualInterestRate = 0.15
# balance =  16768
# high= ((balance * annualInterestRate)+balance)/12
# low = balance/12
# newBalance = balance
# endBalance = balance
# epsilon = .02

# while endBalance > epsilon or endBalance < 0:
#     newBalance = balance
#     monthlyPayment = (low + high)/2
#     if endBalance > 0 and endBalance < .2:
#         print(round(monthlyPayment, 2))
#         break
#     elif endBalance > 0:
#         high = monthlyPayment
#     elif endBalance < 0:
#         low = monthlyPayment
#     for i in range(12):
#         montlyInterestRate = annualInterestRate/12
#         monthlyUnpaidBalance = newBalance - monthlyPayment
#         newBalance = monthlyUnpaidBalance + (monthlyUnpaidBalance * montlyInterestRate)
#     endBalance = newBalance
#     print(round(monthlyPayment, 2))

# annualInterestRate = 0.15
# balance =  16768
# high= ((balance * annualInterestRate)+balance)/12
# low = balance/12
# newBalance = balance
# endBalance = balance
# epsilon = .02

# while endBalance > epsilon or endBalance < 0:
#     newBalance = balance
#     monthlyPayment = (low + high)/2
#     for i in range(12):
#         montlyInterestRate = annualInterestRate/12
#         monthlyUnpaidBalance = newBalance - monthlyPayment
#         newBalance = monthlyUnpaidBalance + (monthlyUnpaidBalance * montlyInterestRate)
#     endBalance = newBalance
#     if endBalance > -.2 and endBalance < .2:
#         print(round(monthlyPayment, 2))
#         break
#     elif endBalance > 0:
#         monthlyPayment = high
#     elif endBalance < 0:
#         monthlyPayment = low
#     print(round(monthlyPayment, 2))

#works
annualInterestRate = 0.15
balance =  16768
high= ((balance * annualInterestRate)+balance)/12
low = balance/12
newBalance = balance
endBalance = balance
epsilon = .02

while endBalance > epsilon or endBalance < 0:
    newBalance = balance
    monthlyPayment = (low + high)/2
    for i in range(12):
        montlyInterestRate = annualInterestRate/12
        monthlyUnpaidBalance = newBalance - monthlyPayment
        newBalance = monthlyUnpaidBalance + (monthlyUnpaidBalance * montlyInterestRate)
    endBalance = newBalance
    if endBalance > 0 and endBalance < .2:
        print(round(monthlyPayment, 2))
        break
    elif endBalance > 0:
        low = monthlyPayment
    elif endBalance < 0:
        high = monthlyPayment
print(round(monthlyPayment, 2))
    
# low = balance/12
# high= ((balance * annualInterestRate)+balance)/12
# monthlyPayment = (low + high)/2
# newBalance = balance
# epsilon = .01


# while newBalance - (monthlyPayment * 12) > epsilon:
#     newBalance = balance
#     monthlyPayment = (low + high)/2 
#     for i in range(12):
#         montlyInterestRate = annualInterestRate/12
#         monthlyUnpaidBalance = newBalance - monthlyPayment
#         newBalance = monthlyUnpaidBalance + (monthlyUnpaidBalance * montlyInterestRate)
    
# print(round(monthlyPayment, 2))