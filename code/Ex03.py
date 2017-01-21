#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 12:05:36 2017

@author: huy
"""
from __future__ import print_function

from nltk.tokenize import word_tokenize
import string
import re

def tokenize(string):
    index = 0
    d = []
    for i in range(len(string)):
        if (string[i] == ' '):
            d.append(string[index:i])
            index = i+1
    temp = ',.:;?!'
    for item in range(len(d)):
        if d[item][-1] in temp:
            d[item] = d[item].replace(d[item][-1], '')
            
    return d
    

if __name__ == '__main__':
    sen = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
    d = tokenize(sen)
    for i in d:
        print('{}__{}'.format(i, len(i)))
        

