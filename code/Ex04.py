#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 13:22:36 2017

@author: huy
"""

from __future__ import print_function

import numpy as np

def main():
    sen = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
    words = sen.split()
    index = np.array([1, 5, 6, 7, 8, 9, 15, 16, 19])
    index = index - 1
    
    d = {}
    for i in range(len(words)):
        if i in index:
            temp = words[i][:1]
        else:
            temp = words[i][:2]
        if temp in d:
            continue
        else:
            d[temp] = i+1

    print(d)

if __name__ == '__main__':
    main()

    
    