#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 13:46:47 2017

@author: huy
"""

def make_words_ngrams(sen, n):
    words = sen.split()
    temp = ',.:;?!'
    for item in range(len(words)):
        if words[item][-1] in temp:
            words[item] = words[item].replace(words[item][-1], '')
            
    assert n <= len(words)
    temp = []
    iteration = len(words) - (n-1)
    for i in range(iteration):
        temp.append(words[i:i+n])
    
    return temp
    
def make_char_ngram(sen, n):
    assert n <= len(sen)
    temp = []
    iteration = len(sen) - (n-1)
    for i in range(iteration):
        temp.append(sen[i:i+n])
        
    return temp
    
if __name__ == '__main__':
    sen = "I am an NLPer"
    print(make_words_ngrams(sen,2))
    print(make_char_ngram(sen,2))