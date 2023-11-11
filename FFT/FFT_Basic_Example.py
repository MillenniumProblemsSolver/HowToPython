# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 07:27:01 2021

@author: a.herrmann
"""


import numpy as np
import matplotlib.pyplot as plt

# close all figures
plt.close('all')

timeBase = np.linspace(0,1000,1001)
omega = (2*np.pi)/(10)
# do data import
data = np.sin(timeBase*omega)

# do fft
fftData = np.fft.fft(data)
fftFrequency = np.fft.fftfreq(len(timeBase), d=1)

# plot data
plt.plot(timeBase,data)
plt.figure(2)
plt.plot(fftFrequency,abs(fftData))

