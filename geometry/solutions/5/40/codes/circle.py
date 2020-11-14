#Code by GVV Sharma
#November 25, 2019
#released under GNU GPL

#This program plots the circumcircle of Triangle ABC
import numpy as np
import matplotlib.pyplot as plt
from coeffs import *
#from circumcentre import  ccircle
#if using termux
import subprocess
import shlex
#end if
G = np.array([-10,-5])
S = np.array([10,-5])
O = np.array([0,0])
A = np.array([-np.sqrt(75),-5])
B = np.array([-np.sqrt(24),-5])
C = np.array([np.sqrt(24),-5])
D = np.array([np.sqrt(75),-5])
M = np.array([0,-5])

x_random = line_gen(G,S)
x_OM = line_gen(O,M)
x_OA = line_gen(O,A)
x_OB = line_gen(O,B)
x_OC = line_gen(O,C)
x_OD = line_gen(O,D)


len = 200
theta = np.linspace(0,2*np.pi,len)
x_circ = np.zeros((2,len))
y_circ = np.zeros((2,len))
x_circ[0,:] = 7*np.cos(theta)
x_circ[1,:] = 7*np.sin(theta)
y_circ[0,:] = 10*np.cos(theta)
y_circ[1,:] = 10*np.sin(theta)
x_circ = (x_circ.T + 0).T
y_circ = (y_circ.T + 0).T

plt.plot(x_random[0,:],x_random[1,:],label='$ABCD$')
plt.plot(x_OM[0,:],x_OM[1,:],linestyle='dotted',label='$OM$')
plt.plot(x_OA[0,:],x_OA[1,:],linestyle='dotted',label='$OA$')
plt.plot(x_OB[0,:],x_OB[1,:],linestyle='dotted',label='$OB$')
plt.plot(x_OC[0,:],x_OC[1,:],linestyle='dotted',label='$OC$')
plt.plot(x_OD[0,:],x_OD[1,:],linestyle='dotted',label='$OD$')

plt.plot(x_circ[0,:],x_circ[1,:],label='$circle 1$')
plt.plot(y_circ[0,:],y_circ[1,:],label='$circle 2$')

plt.text( -np.sqrt(75)* (1.1), -5 * (1.2) , 'A')
plt.text( -np.sqrt(24)* (1.2), -5 * (1.2) , 'B')
plt.text( np.sqrt(24)* (1.2), -5 * (1.2) , 'C')
plt.text( np.sqrt(75)* (1.1), -5 * (1.2) , 'D')
plt.text(0,-5*(1.2),'M')
plt.text(0,0,'O')
plt.axis('equal')
plt.legend(loc = 'upper right')
plt.show()