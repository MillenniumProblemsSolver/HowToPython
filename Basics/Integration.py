#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  8 18:02:13 2021

@author: kernelm0de
"""

# import some module
from scipy.integrate import quad

#define function 
def f(x):
    return x

# integrate function
print(quad(f, 0,1))

# first define a function
def g(x):
    return -x + 2

# do the integarion form 0 to inf
print(quad(g,0,1))