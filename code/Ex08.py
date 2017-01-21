#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 14:34:21 2017

@author: huy
"""

import string
import re

def cipher(string):
    newstring = ''
    for i in string:
        if i.islower():
            i = chr(219 - ord(i))
        newstring += i
        
    return newstring
    
def decipher(string):
    newstring = ''
    for i in string:
        if i.islower():
            i = chr(219 - ord(i))
            
        newstring += i
        
    return newstring
    
if __name__== '__main__':
    s = 'GiaHuyDangNguyenThuongHien'
    s1 = cipher(s)
    print s1
    print(decipher(s1))