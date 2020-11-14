#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 16:56:18 2020

@author: shantanu
"""

' Matrix Theory : Assignment 1 : Shantanu Yadav : EE20MTECH12001'
'Problem Statement : Find the equations of the lines which have intercepts on'
'on axes whose sum and product are 1 and -6 respectively.'
'The intercepts are solved using the two equations a+ b =1 a*b=-6'
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import math

axes = plt.gca()
plt.grid()


sum_of_roots = 1
product_of_roots = -6

# x^2 - (sum of roots)x + (product of roots) = 0
#discriminant
d = (sum_of_roots**2) - (4*product_of_roots)

#calculating intercepts 
x_intercept_1 = ((sum_of_roots) + math.sqrt(d))/2
x_intercept_2 = ((sum_of_roots) - math.sqrt(d))/2

y_intercept_1 = sum_of_roots - x_intercept_1
y_intercept_2 = sum_of_roots - x_intercept_2



print("The x and y intercept of line 1 are : ", x_intercept_1," ",y_intercept_1,"respectively")
print("The x and y intercept of line 2 are : ", x_intercept_2," ",y_intercept_2,"respectively")




x_vals = np.arange(-8,6,1)

#line1
y_vals = y_intercept_1  - (y_intercept_1/x_intercept_1) * x_vals
#line2
y_vals1 = y_intercept_2 - (y_intercept_2/x_intercept_2) *  x_vals


#plotting
line,=plt.plot(x_vals, y_vals,'b-')
line.set_label('y = 1.5x + 3')
line_2,=plt.plot(x_vals,y_vals1,'r-' )
line_2.set_label('y = 0.667x - 2')

#marking the plot
plt.xticks(np.arange(min(x_vals), max(x_vals)+1, 1.0))
plt.yticks(np.arange(-10, 10, 1.0))
plt.legend()

#marking the coordinates
plt.plot(x_intercept_1,0,'o-',0,y_intercept_1,'o-')
plt.annotate("  x-intercept (3,0)",(x_intercept_1,0))
plt.annotate("  y-intercept(0,-2)",(0,y_intercept_1))
plt.plot(x_intercept_2,0,'o-',0,y_intercept_2,'o-')
plt.annotate("  x-intercept (-2,0)",(x_intercept_2,0))
plt.annotate("  y-intercept(0,3)",(0,y_intercept_2))
    