#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 15:30:15 2021

@author: Hybridkernel
"""

# open file with write permission
f = open('FileIO.txt', 'w')
#write file
f.write("Hello World!")
#close file
f.close()

# open file with read permission
f = open('FileIO.txt', 'r')
#read file
print(f.read())
#close file 
f.close()

# see docu on https://docs.python.org/3/tutorial/inputoutput.html

