#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 16:06:09 2021

@author: Hybridkernel
"""
# create hash table
Dict = {3:"int",10:"char"} 
#print elements
print (Dict[3])
# set element 
Dict[3]="This is a test"
# print it once again
print (Dict[3])

# the other way 
# create hash table
Dict = {"int":3,"char":10} 
#print elements
print (Dict["int"])
# set element 
Dict["int"]=22
# print it once again
print (Dict["int"])

# see also doku https://docs.python.org/3/tutorial/datastructures.html#dictionaries