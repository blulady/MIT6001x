# -*- coding: utf-8 -*-
"""
Created on Mon Jun 21 19:05:48 2021

@author: Sarah
"""

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    guess = []
    matching = []
    for letters in lettersGuessed:
        if letters in secretWord:
            matching.append(letters)
    print(matching)
    for letters in secretWord:
        if letters in matching:
            guess.append(letters)
    return len(guess) == len(secretWord)
    
    
secretWord = 'apple'
lettersGuessed = ['a', 'p', 'p', 'l', 'e']
#lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print(isWordGuessed(secretWord, lettersGuessed))


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # guessedWord = ''
    # for letter in secretWord:
    #     guessedWord += '_ '
    # for letter in range(len(secretWord)):
    #     if secretWord[letter] in lettersGuessed:
    #         guessedWord[letter*2] 
    
    guessedWord = ''
    # for letter in secretWord:
    #     guessedWord += '_'
    # for letter in range(len(secretWord)):
    #     if secretWord[letter] in lettersGuessed:
    #         #guessedWord[letter] = secretWord[letter]
    #         guessedWord += secretWord[letter]
    for letter in range(len(secretWord)):
        if secretWord[letter] in lettersGuessed:
            guessedWord += secretWord[letter]
        else:
            guessedWord += '_ '
    return guessedWord
    
            
            

    
    
    
secretWord = 'apple' 
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print(getGuessedWord(secretWord, lettersGuessed))
#'_ pp_ e'  

import string

def getAvailableLetters(lettersGuessed):
    
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.  '''
    alpha = string.ascii_lowercase
    alphaNoLettersGuessed = ''
    for letter in alpha:
        if letter not in lettersGuessed:
            alphaNoLettersGuessed += letter
    return alphaNoLettersGuessed
    
      
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print(getAvailableLetters(lettersGuessed))
