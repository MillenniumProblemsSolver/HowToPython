#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  7 20:28:45 2021

@author: Hybridkernel
"""

# a simple example of a class
class vehicle: 
    
    # constructor 
    def __init__ (self,brand):
        # self is the class 
        self.power = 0.0
        if type(brand) is not str:
            print("brand is not a string")
        else:
            self.brand = brand
        
    # some function
    def printBrand(self):
        print(self.brand)
        
    # abstract method
    def PrintAmountOfTires(self):
        pass


# another class inheriting from vehicle
class car(vehicle):
    def PrintAmountOfTires(self):
        print('4 Tires')
    
    
    
testvehicle = vehicle('TestBrand')
testvehicle.printBrand()    

testcar = car('AnotherTestBrand')
testcar.PrintAmountOfTires()