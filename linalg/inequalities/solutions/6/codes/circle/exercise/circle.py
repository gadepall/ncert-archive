import numpy as np 
import matplotlib.pyplot as plt 
from coeffs import *
import subprocess
import shlex

A = np.array([4,1])
B = np.array([6,5])
O = np.array([3,4])

x_OA = line_gen(O,A)
x_OB = line_gen(O,B)
len = 200
theta = np.linspace(0,2*np.pi,len)
x_circ = np.zeros((2,len))
x_circ[0,:] = np.sqrt(10)*np.cos(theta)
x_circ[1,:] = np.sqrt(10)*np.sin(theta)
x_circ = (x_circ.T + O).T

plt.plot(x_circ[0,:],x_circ[1,:],label='$circle$')
plt.plot(A[0],A[1],'o')
plt.plot(B[0],B[1],'o')
plt.plot(O[0],O[1],'o')
plt.plot(x_OA[0,:],x_OA[1,:],linestyle='dotted')
plt.plot(x_OB[0,:],x_OB[1,:],linestyle='dotted')


plt.text(A[0]+0.5,A[1],'A')
plt.text(B[0]+0.5,B[1],'B')
plt.text(O[0],O[1]+0.5,'O')

plt.xlabel('x')
plt.ylabel('y')
plt.axis('equal')
plt.legend(loc = 'upper right')
plt.show()