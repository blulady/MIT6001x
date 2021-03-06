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
    
    
# secretWord = 'apple'
# lettersGuessed = ['a', 'p', 'p', 'l', 'e']
# #lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
# print(isWordGuessed(secretWord, lettersGuessed))


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
    
            
            

    
    
    
# secretWord = 'apple' 
# lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
# print(getGuessedWord(secretWord, lettersGuessed))
# #'_ pp_ e'  

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
    
      
# lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
# print(getAvailableLetters(lettersGuessed))

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    
    secretWordLength = len(secretWord)
    print('Welcome to the game Hangman!\nI am thinking of a word that is ' + str(secretWordLength) + ' letters long\n-------------')
    guessesLeft = 8
    lettersGuessed = []
    
    while guessesLeft != 0:
        newGuess = input("You have "+ str(guessesLeft) +" guesses left\nAvailable Letters: " + getAvailableLetters(lettersGuessed)+ "\nPlease guess a letter: " )
        newGuess = newGuess.lower()
        if newGuess in lettersGuessed:
            print("Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed))
            print("------------")
        elif newGuess in secretWord:
            lettersGuessed.append(newGuess)
            print("Good guess: " + getGuessedWord(secretWord, lettersGuessed ))
            print("------------")
        #elif newGuess == lettersGuessed[-1]:
            #print('Congratulations, you won!')
            #break
        else:
            guessesLeft -=1
            lettersGuessed.append(newGuess)
            print("Oops! That letter is not in my word: " + getGuessedWord(secretWord, lettersGuessed), "\n-------------")

    if guessesLeft == 0:
        print('Sorry, you ran out of guesses. The word was ' + secretWord +'.')
    elif guessesLeft > 0:
        print('Congratulations, you won!')
        
