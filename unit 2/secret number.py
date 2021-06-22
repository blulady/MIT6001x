# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 12:03:14 2021

@author: Sarah
"""
ans = 46
high =100 
low = 0
accept = ['c','l','h']
guess = (high + low)/2
    
x = input("Please think of a number between 0 and 100!\nIs your secret number " + str(guess)+"?\n"
"Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")

while x != 'c':
    if x == 'h':
        high = guess
        guess = int((high + low)//2)
        x = input("Is your secret number " + str(guess)+"? \nEnter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    elif x == 'l':
        low = guess 
        guess = int((high + low)//2)
        x = input("Is your secret number " + str(guess)+"? \nEnter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    elif x not in accept:
        x = input("Sorry, I did not understand your input.\n Is your secret number " + str(guess)+"?\nEnter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
if x == 'c':
    print('Game over. Your secret number was:', guess)

    
    
    
# ans = 46
# high =100 
# low = 0

# guess = (high + low)/2
    
# x = input("Please think of a number between 0 and 100!\nIs your secret number " + str(guess)+"?\n"
# "Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")

# while x != 'c':
#     if x == 'h':
#         high = guess
#         guess = (high + low)/2
#         x = input("Is your secret number " + str(guess)+"? Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
        
#     else:
#         low = guess 
#         guess = (high + low)/2
#         x = input("Is your secret number " + str(guess)+"? Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
# if x == 'c':
#     print('Game over. Your secret number was:', guess)
# if x != 'c' or 'h' or 'l':
#     x = input("Sorry, I did not understand your input.\n Is your secret number " + str(guess)+"?")

    

          