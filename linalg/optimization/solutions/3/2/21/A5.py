# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 03:23:26 2020

@author: Hrithik
"""

import numpy as np
import matplotlib.pyplot as plt
import math



# equation - y^2 = 4x
X_coord = np.array(np.linspace(0, 5.0, num=40))
Y_coord =[math.sqrt(4*num) for num in X_coord]
y1 = np.zeros(len(X_coord))

for i in range(len(X_coord)):
    y1[i] = Y_coord[i]*-1


#plot points and lines
plt.plot(X_coord, Y_coord,'r', label='$y^2=4x$')
plt.plot(X_coord, y1,'r')
plt.plot(1, 2, 'o', label='Point of contact q=(1,2)')
X_coord = np.array(np.linspace(-3, 4.0, num=40))
y2= 1 + X_coord
plt.plot(X_coord,y2,  label='y = x + 1 ') #Since m = 1   
#plt.text(1, 2)



plt.axis('equal')
plt.legend(loc='best')
plt.grid()
plt.show()