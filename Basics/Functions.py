#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 21:26:08 2021

@author: Hybridkernel
"""

#first test function
def testfunction():
    print("this is a test")
    
testfunction()

# function with a return value
def addition():
    return 1+2

print("1+2="+str(addition()))

#function with a spicific return type
def division()->float:
    return 1.0/2.0

print("1.0/2.0="+str(division()))

#function with parameters
def multiplication(x:float,y:float)->float:
    return x*y

print("5.8*7.3="+str(multiplication(5.8,7.3)))