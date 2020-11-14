#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 16:56:18 2020

@author: shantanu
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import math

axes = plt.gca()
plt.grid()


#calculating intercepts 
x_intercept_1 = 1.75
x_intercept_2 = 0.6667

y_intercept_1 =85.75/37
y_intercept_2 = -1

x_vals = np.arange(-1,8,1)

#line1
y_vals = y_intercept_1  - (y_intercept_1/x_intercept_1) * x_vals
#line2
y_vals1 = y_intercept_2 - (y_intercept_2/x_intercept_2) *  x_vals


#plotting
line,=plt.plot(x_vals, y_vals,'b-')
line.set_label('y = -49/37x + 85.75/37')
line_2,=plt.plot(x_vals,y_vals1,'r-' )
line_2.set_label('y = 51/34x - 1')

#marking the plot
plt.xticks(np.arange(min(x_vals), max(x_vals)+1, 1.0))
plt.yticks(np.arange(-9, 10, 1.0))
plt.legend()

#marking the coordinates
plt.plot(1.17,0.76,'ro')
plt.annotate(" Point of intersection (1.17,0.76)",(1.17,0.76))
    