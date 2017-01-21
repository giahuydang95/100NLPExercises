#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 14:34:40 2017

@author: huy
"""

import numpy as np

def Typolycemia(sen):
    newsen = ''
    words = sen.split()
    for word in words:
        if len(word) <= 3:
            newword = word
        else:
            newword = word[0]
            mid = len(word) - 2
            index = np.arange(1,len(word)-1)
            np.random.shuffle(index)
            for j in index:
                newword += word[j]
            newword += word[-1]
        if word == words[-1]:
            newsen  += newword
        else:
            newsen += newword + ' '
        
    return newsen
    
if __name__ == '__main__':
    sen = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
    print(Typolycemia(sen))