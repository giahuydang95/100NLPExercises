#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 11:56:00 2017

@author: huy
"""

def EvenSplitting(string):
    temp = []
    index = range(1,(len(string)+1),2)
    for i in index:
        temp.append(string[i])
        
    return ''.join(temp)
    
if __name__ == '__main__':
     string = "MPyaktQrBoilk RCSahr"
     print(EvenSplitting(string))