#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 11:33:32 2021

@author: kernelm0de
"""

# some needed imports
import numpy as np
import matplotlib.pyplot as plt

# autosclose all open diagramms
plt.close('all')

# values
omega1 = (2*np.pi)/200.0 # pulsatance signal 1
omega2 = (2*np.pi)/500.0 # pulsatance signal 2
omega3 = (2*np.pi)/100.0 # pulsatance signal 3

# generate signals
x = np.linspace(0,1000,1001) # in msec
y1 = np.sin(omega1*x)
y2 = np.sin(omega2*x)
y3 = np.sin(omega3*x)

# see documentation 
# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html

# generate subplots
Window,(Diagram1,Diagram2) = plt.subplots(1,2)  # number of rows = 1 
                                                # number of columns = 2

# plot signal 1
Diagram1.plot(x,y1)
Diagram1.set_title('Signal 1')
Diagram1.set_xlabel('x label')
Diagram1.set_ylabel('y label')

# plot signal 2 with color magenta
Diagram2.plot(x,y2,'m')
Diagram2.set_title('Signal 2')
Diagram2.set_xlabel('x label')

# generate new diagram
plt.figure(2)

# plot signal 3 with color and other shape dashed red 
plt.plot(x,y3,'r--')

# add axis labeling
plt.xlabel('time in msec')
plt.ylabel('voltage in V')