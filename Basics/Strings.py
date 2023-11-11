#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 20:12:30 2021

@author: Hybridkernel
"""

# store a string in a variable
SomeText = "Hello World !"

# print the text
print(SomeText)

# print first char of the string
print(SomeText[0])

#print Hello
print(SomeText[0:5])

# store a string with erveral lines
AnotherText = """ 
                  Hello
                  World
                  !"""
                  
# print last text
print(AnotherText)

# check it there is a W in the string
print('W' in AnotherText)

# check it there is a World in the string
print('World' in AnotherText)

# check it there is a Moon in the string
print('Moon' in AnotherText)

# print string length 
print(len(SomeText))

# do some operations
string1 = "Hello"
string2 = "World"

#print both strings
print(string1 + " " + string2)

#replace a char
print(string1.replace('l','t'))

# print in upper and lower case
print(string1.upper())
print(string1.lower())

# split string in seperate values
print(SomeText.split(" "))

# print special chars
print("Hello \"World\" !")

#  find somethind in a string  
print('you can find World at postion: ' + str( SomeText.find('World')))

# count how often there is a subsring
print('you can find World ' + str( SomeText.count('World')) + ' time in the \n string')

# strings ae objects with much more functions
# see https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str