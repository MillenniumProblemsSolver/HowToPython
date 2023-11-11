#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 11:33:32 2021

@author: kernelm0de
"""

# some needed imports
import numpy as np
import matplotlib.pyplot as plt

# values
omega = (2*np.pi)/200.0 # pulsatance

# generate signal
x = np.linspace(0,1000,1001) # in msec
y = np.sin(omega*x)

# plot signal
plt.plot(x,y)
