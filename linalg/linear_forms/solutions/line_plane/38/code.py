# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 07:25:02 2020

@author: Jayanth
"""


import numpy as np
import matplotlib.pyplot as plt
import math


def magnitude(A):
    return np.sqrt(A[0]**2+A[1]**2)

#Given Vectors
A = np.array([-np.sqrt(3),1])
B = np.array([-1,np.sqrt(3)])

#Length vectors
mag_A = magnitude(A)
mag_B = magnitude(B)

#Finding Angle

cos_ang = (A.T@B)/(mag_A*mag_B)
ang = math.acos(cos_ang)

#figure
x1 = np.linspace(-10,10,100)
y1 = 1-np.sqrt(3)*x1


x2 = np.linspace(-10,10,100)
y2 = 1-np.sqrt(1/3)*x2;

plt.plot(x1, y1, '-r',label='Line(i)')

plt.xlabel('x', color='b')
plt.ylabel('y', color='g')


plt.plot(x2, y2, '-b',label='Line(ii)')

plt.xlabel('x', color='b')
plt.ylabel('y', color='g')


print("Angle between Lines(in radians) :",ang)


