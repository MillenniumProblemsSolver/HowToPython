#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 14:51:59 2021

@author: kernelm0de
"""

import gc

# create an array
u = [1.0,2.0,3.0,4.0,5.0]
v = ["this","is","a","test"]
# print the values
print(u)
print(v)
# free the arrays
u = None
v = None
# run garbage collector
gc.collect()