# -*- coding: utf-8 -*-
"""
Created on Mon Jun 21 12:19:48 2021

@author: Sarah
"""

lyrics = "Too young Too young Too young Too young Too young Too young Oh Too young Oh Too young Oh Too young Oh Too young Oh Girl the night's not over Oh too young We're not getting older Oh too young They can chase forever Oh too young Cause in the morning Oh too young There's a million names to choose from You don't care just take one Leave a place to rest on Because you're too young Too young Uh Yeah you're too young Too young Uh Oh you're too young Too young Uh You're too young Too young Oh Too young Oh Too young Oh Too young Oh Too young Oh Too young Uh Too young Uh Too young UhToo young Uh"
lyricList = lyrics.split(' ')
def lyrics_to_freq(lyrics):
    myDict = {}
    for word in lyrics:
        if word in myDict:
            myDict[word] += 1
        else:
            myDict[word] = 1
    return myDict

junior_boys = lyrics_to_freq(lyricList)

def most_common_words(freqs):
    values = freqs.values()
    best = max(freqs.values())
    words = []
    for k in freqs: 
        if freqs[k] == best:
            words.append(k)
    return(words, best)
    
# def words_often(freqs, minTimes):
#     result = []
#     done = False
#     while not done:
#         temp = most_common_words(freqs)
#         if temp[1] >= minTimes:
#             result.append(temp)
#             for w in temp[0]:
#                 del(freqs[w])  #remove word from dictionary
#         else:
#             done = True
#     return result
    
# print(words_often(beatles, 5))

def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    count = 0
    for elem in map(len, aDict.values()):
        count += elem
    return count



def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''

    # biggest = 1
    # for k,v in aDict.items():
    #     if len(v) > biggest:
    #         biggest = len(v)
    #         print(k)
    
    values = aDict.values()
    best = max(values)
    #words = []
    #words = ''
    for k in aDict:
        if aDict[k] == best:
            return k
            #words += aDict[k]
            #words.append(k)
    #return words
    

def fib_memoization(n, d):
    if n in d:
        return d[n]
    else:
        ans = fib_memoization(n -1, d) + fib_memoization(n-2, d)
        d[n] = ans
        return ans
    
d = {1:1, 2:2}

#changin the dict for git
#adding more changes where my codes at
#make some new text to be added to file