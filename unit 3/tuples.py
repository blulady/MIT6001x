# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 19:04:40 2021

@author: Sarah
"""

def get_data(aTuple):
    nums = ()
    words = ()
    for t in aTuple:
        nums = nums + (t[0],)
        if t[1] not in words:
            words = words + (t[1])
    min_nums = min(nums)
    max_nums = max(nums)
    unique_words = len(words)
    return(min_nums, max_nums, unique_words)


def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    # this version returns odd odd numbered tuples
    #ie oddTuples((6, 12, 8, 11, 13, 11)) >>> (11, 13, 11)
    oddTup = ()
    for i in aTup:
        if i % 2!= 0:
            oddTup += (i,)
    return oddTup

def oddTuples2(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''

    oddTup = ()
    for i in range(len(aTup)):
        if i % 2== 0:
            oddTup += (aTup[i],)
    return oddTup