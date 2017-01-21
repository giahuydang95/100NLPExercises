#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 14:08:43 2017

@author: huy
"""
import numpy as np

from Ex05 import make_char_ngram

def main():
    s1 = 'paraparaparadise'
    s2 = 'paragraph'
    
    X = np.array(make_char_ngram(s1, 2))
    Y = np.array(make_char_ngram(s2, 2))
    
    X = np.unique(X)
    Y = np.unique(Y)
    
    temp = [X[i] in Y for i in range(len(X))]
    intersect = [X[i] for i in range(len(temp)) if temp[i] == True]
    union = (np.unique(np.concatenate((X,Y)))).tolist()
    temp2 = [i not in intersect for i in union ]
    different = [union[i] for i in range(len(temp2)) if temp2[i] == True]
    
    return union, intersect, different
    
if __name__ == '__main__':
    union, intersect, different = main()
    print('Union', union)
    print('Intersect', intersect)
    print('Different', different)
    
    
    
    
    
